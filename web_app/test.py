from PIL import Image, ImageEnhance

# Charger l'image
image = Image.open("/home/ebwala/Documents/projet_yolo/datasets/images/valid/4fc2e7c9-Cars55.png")

# Appliquer une réduction de la luminosité pour simuler une faible luminosité
enhancer = ImageEnhance.Brightness(image)
low_light_image = enhancer.enhance(0.3)  # Réduction de la luminosité

# Enregistrer l'image modifiée
low_light_image.save("/home/ebwala/Documents/projet_yolo/datasets/images/test/scenario_test5.png")
