import cv2
import os
import yaml
from sklearn.model_selection import train_test_split

# root_dir = "datasets/car-number-plat/"
# valid_formats = [".png", ".jpg", ".txt"]

# def file_paths(root, valid_formats):
#     file_paths = []
#     for dirpath, dirnames, filenames in os.walk(root):
#         for filename in filenames:
#             extension = os.path.splitext(filename)[1].lower()
#             if extension in valid_formats:
#                 file_path = os.path.join(dirpath, filename)
#                 file_paths.append(file_path)
#     return file_paths

# # Récupérons  les chemins des images et des labels
# image_paths = file_paths(root_dir + "images", valid_formats[:2])  # Formats d'images : .png, .jpg
# label_paths = file_paths(root_dir + "labels", valid_formats[2])  # Format des labels : .txt

# # Convertir les listes de chemins en dictionnaires pour vérifier les correspondances
# def paths_to_dict(paths):
#     return {os.path.splitext(os.path.basename(path))[0]: path for path in paths}

# image_dict = paths_to_dict(image_paths)
# label_dict = paths_to_dict(label_paths)

# # Trouvons les noms de fichiers communs dans les deux ensembles
# common_names = set(image_dict.keys()).intersection(set(label_dict.keys()))

# # Filtrons les chemins des images et des labels pour ne conserver que ceux avec des correspondances
# image_paths = [image_dict[name] for name in common_names]
# label_paths = [label_dict[name] for name in common_names]


# # Division des données
# X_train, X_valid_test, y_train, y_valid_test = train_test_split(image_paths, label_paths, test_size=0.3, random_state=42)
# X_valid, X_test, y_valid, y_test = train_test_split(X_valid_test, y_valid_test, test_size=0.7, random_state=42)

# def write_to_file(images_path, labels_path, X):
#     os.makedirs(images_path, exist_ok=True)
#     os.makedirs(labels_path, exist_ok=True)

#     for image_path in X:
#         img_name = os.path.splitext(os.path.basename(image_path))[0]
#         img_ext = os.path.splitext(os.path.basename(image_path))[1]

#         # Sauvegarde d'image
#         image = cv2.imread(image_path)
#         cv2.imwrite(f"{images_path}/{img_name}{img_ext}", image)

#         # Sauvegarde de label
#         label_path = f"{root_dir}/labels/{img_name}.txt"
#         with open(label_path, "r") as label_file:
#             label_data = label_file.read()
        
#         with open(f"{labels_path}/{img_name}.txt", "w") as f:
#             f.write(label_data)

# # Sauvegarde des ensembles de données
# write_to_file("datasets/images/train", "datasets/labels/train", X_train)
# write_to_file("datasets/images/valid", "datasets/labels/valid", X_valid)
# write_to_file("datasets/images/test", "datasets/labels/test", X_test)


data ={
    "path":"../datasets",
    "train":"images/train",
    "train":"images/valid",
    "train":"images/test",

    "names":["number plate"]

}
with open("number-plate.yaml", "w") as f:
    yaml.dump(data, f)