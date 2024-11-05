import streamlit as st
from ultralytics import YOLO
from easyocr import Reader
import time
import cv2
import os
import sys

sys.path.append('/home/ebwala/Documents/projet_yolo')
from detect_and_recognize import detect_number_plates, recognize_number_plates

st.set_page_config(page_title="Auto NRP", page_icon=":car:", layout="wide")

st.title("DRC Automatic Number Plate Recognition System :car:")
st.markdown("---")


st.sidebar.image("logo.png", width=150) 
st.sidebar.title("Options de Détection")


detection_source = st.sidebar.selectbox(
    "Detection from :", ["File", "Webcam", "RTSP Stream"]
)

save_crops = st.sidebar.selectbox("Do you want to save Crops ?", ["Yes", "No"])

compute_device = st.sidebar.selectbox("Select compute Device :", ["CPU", "GPU"])

save_output = st.sidebar.radio("Save output video?", ["Yes", "No"])


confidence_threshold = st.sidebar.slider(
    "Select threshold confidence value :", 0.1, 1.0, 0.25
)

st.sidebar.markdown("---")


uploaded_file = st.file_uploader("Upload an Image or Video", type=["png", "jpg", "jpeg", "mp4", "mkv"])
upload_path = "uploads"

if uploaded_file is not None:
    
    file_path = os.path.sep.join([upload_path, uploaded_file.name])
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    is_video = uploaded_file.type in ["video/mp4", "video/mkv"]
    
    with st.spinner("Processing..."):
        model = YOLO("../runs/detect/train/weights/best.pt")
        reader = Reader(['en'], gpu=compute_device == "GPU")

       
        if is_video:
            cap = cv2.VideoCapture(file_path)
            stframe = st.empty()  
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                    #depetction de la plaque 
                number_plate_list,_ = detect_number_plates(frame, model)
                if number_plate_list != []:
                    recognized_plate_list = recognize_number_plates(frame, reader, number_plate_list)
                    for box, text in number_plate_list:
                        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                        cv2.putText(frame, text, (box[0], box[3] + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

               #lecture video , image
                stframe.image(frame, channels="BGR")
            cap.release()
        else:
            
            image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
            image_copy = image.copy()

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Image")
                st.image(image)

            number_plate_list,confidences = detect_number_plates(image, model)
            

            if number_plate_list != []:
                recognized_plate_list = recognize_number_plates(file_path, reader, number_plate_list)

                for idx, (box, text) in enumerate(number_plate_list):
                    #if confidences!=[] and  confidences[idx]>=0.5:
                    cropp_number_plate = image_copy[box[1]:box[3], box[0]:box[2]]

                
                    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
                    cv2.putText(image, text, (box[0], box[3] + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

                    with col2:
                        st.subheader("Number Plate Detection")
                        st.image(image)

                    st.subheader("Cropped Number Plate")
                    st.image(cropp_number_plate)
                    st.success(f"Extracted number plate text: **{text}**")

                    st.markdown(f"### Recognized License Plate Number: **{text}**")

                    if confidences!=[]:
                        print("index ============ ",idx)
                        if confidences[idx]:
                            st.markdown("confidence ======: {:.2f}%".format(confidences[idx] * 100))  
            else:
                st.error("No number plate detected.")
else:
    st.info("Please upload an image or video to get started.")
