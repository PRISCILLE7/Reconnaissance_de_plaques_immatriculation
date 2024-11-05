from ultralytics import YOLO
from easyocr import Reader
import time
import torch
import cv2
import os
import csv

CONFIDENCE_THRESHOLD = 0.4
COLOR = [0, 255, 0]

def detect_number_plates(image, model, display=False):
    start = time.time()

    detections = model.predict(image)[0].boxes.data
    
    if detections.shape != torch.Size([0, 6]):

        boxes = []
        confidences = []
        
        for detection in detections:
            confidence = detection[4]

            if float(confidence) < CONFIDENCE_THRESHOLD:
                continue

            boxes.append(detection[:4])
            confidences.append(detection[4])
        print(f"{len(boxes)} Number plate(s) have been detected.")
        number_plate_list = []
        
        for i in range(len(boxes)):
            xmin, ymin, xmax, ymax = int(boxes[i][0]), int(boxes[i][1]), int(boxes[i][2]), int(boxes[i][3])

            number_plate_list.append([[xmin, ymin, xmax, ymax]])

            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), COLOR, 2)
            print("confidence ======: {:.2f}%".format(confidences[i] * 100))
            text = "Number plate: {:.2f}%".format(confidences[i] * 100)
            cv2.putText(image, text, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLOR, 2)
        
        if display:
            number_plate = image[ymin:ymax, xmin:xmax]
            cv2.imshow(f"Number plate {i}", number_plate)

        end = time.time()
        print(f"Time to detect the number plates: {(end - start) * 1000:.0f} milliseconds")

        return number_plate_list,confidences

    else:
        print("No number plates have been detected")
        return []

def recognize_number_plates(image_or_path, reader, number_plate_list, write_to_csv=False):
    start = time.time()
    image = cv2.imread(image_or_path) if isinstance(image_or_path, str) else image_or_path

    for i, box in enumerate(number_plate_list):
        np_image = image[box[0][1]:box[0][3], box[0][0]:box[0][2]]

        detection = reader.readtext(np_image, paragraph=True)

        if len(detection) == 0:
            text =""
        else:
            text = str(detection[0][1])

        number_plate_list[i].append(text)
    print("===================================================")
    print(number_plate_list)
    if write_to_csv:
        csv_file = open("number_plate", "w")
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["image_path", "box", "text"])

        for box, text in number_plate_list:
            csv_writer.writerow([image_or_path, box, text])

            csv_file.close()

    end = time.time()

    print(f"time to recognize the number plates: {(end - start) * 1000:.0f}milliseconds")
    
    return number_plate_list

if __name__ == "__main__":
    print("Loading model...")
    model = YOLO("runs/detect/train/weights/best.pt")
    reader = Reader(["en"], gpu=False)
    file_path = "datasets/images/test/e438eb13-Cars61.png"
    print(f"File path: {file_path}")

    _, file_extension = os.path.splitext(file_path)
    print(f"File extension: {file_extension}")

    if file_extension.lower() in [".jpg", ".jpeg", ".png"]:
        print("Processing the image...")
        image = cv2.imread(file_path)
        
        #print(f"Image loaded: {image is not None}")
        
        number_plate_list, confidence = detect_number_plates(image, model, display=True)
        
        if number_plate_list !=[]:
            
            recognized_plate_list = recognize_number_plates(file_path, reader, number_plate_list, write_to_csv=True)
           
            for box, text in recognized_plate_list:
                cv2.putText(image, text,(box[0], box[3] +15), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, COLOR, 2)

        cv2.imshow("image", image)
        cv2.waitKey(0)


    elif file_extension.lower() in [".mp4", ".mkv", ".avi", ".wmv", ".mov"]:
        print("Processing video file...")
        
        video_cap = cv2.VideoCapture(file_path)

        frame_width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fps = int(video_cap.get(cv2.CAP_PROP_FPS))

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter("output.mp4", fourcc, fps, (frame_width, frame_height))

        while True:
            start = time.time()  
            success, frame = video_cap.read()

            if not success:
                print("There are no more frames to process. Exiting the script...")
                break

            number_plate_list,_ = detect_number_plates(frame, model)

            end = time.time()

            #fps_display = f"FPS:{1 /(end - start):.2f}"
            #cv2.putText(frame, fps_display, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 8)

            cv2.imshow("Output", frame)
            writer.write(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        video_cap.release()
        writer.release()
        cv2.destroyAllWindows()
        cv2.setNumThreads(0)




