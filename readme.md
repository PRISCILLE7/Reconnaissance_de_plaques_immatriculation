# YOLO-License-Recognition 


**YOLO-License-Recognition** est un projet de reconnaissance de plaques d’immatriculation.
Ce projet vise à développer un système de reconnaissance de plaques d'immatriculation (RPI) pour répondre aux défis spécifiques posés par la gestion de la sécurité et du trafic dans le contexte urbain dynamique de Kinshasa. En utilisant des technologies de pointe telles que la vision par ordinateur avec OpenCV, un modèle YOLOv8 personnalisé pour la détection d'objets, et un OCR (reconnaissance optique de caractères) pour la lecture de texte, ce système s'intègre dans une application Web Streamlit pour fournir une solution complète et accessible.

# Contexte

    Dans un monde où les avancées technologiques redéfinissent sans cesse notre société, la reconnaissance de plaques d’immatriculation est devenue une technologie clé. Elle permet d'apporter des solutions innovantes aux défis contemporains de sécurité et de gestion urbaine. Grâce à la vision par ordinateur, l'apprentissage en profondeur et l'intelligence artificielle, ce projet vise à créer un système de surveillance efficace pour des applications telles que la sécurité routière, la gestion du trafic et la lutte contre la criminalité.

# Problématique

    À Kinshasa, le contrôle de la sécurité routière et de la fluidité du trafic est complexe en raison de l'augmentation constante du nombre de véhicules et de la nécessité d'accéder rapidement et précisément aux données des plaques d'immatriculation. Le système actuel repose en grande partie sur des contrôles manuels qui, en raison des conditions de circulation et de l'insuffisance des infrastructures, ne répondent pas de manière optimale aux besoins croissants en sécurité et mobilité.

    Les principaux défis que ce projet tente de résoudre sont :

    Augmentation constante du nombre de véhicules à gérer : La circulation croissante rend difficile la gestion efficace du trafic.
    Accès rapide et précis aux données des plaques d’immatriculation : Un besoin crucial pour améliorer la réactivité dans la gestion des incidents et la sécurité.
    Intégrité et sécurité des informations collectées : Garantir la confidentialité et la fiabilité des données sensibles.

 Face à ces défis, ce projet propose un système innovant qui utilise des méthodes avancées de reconnaissance d'image et de détection d'objets pour faciliter la gestion du trafic et la sécurité routière.

# Features
1. Reconnaissance de plaques d'immatriculation : Détection des plaques avec un modèle YOLOv8 personnalisé.
2. Extraction de texte via OCR : Lecture des caractères des plaques détectées.
3. Interface Web Streamlit : Accès simplifié via une interface intuitive et interactive.
4. Gestion de données sécurisée : Protection des informations de plaques et des données sensibles collectées.

# Prerequisites
- Python 3.x
- OpenCV, YOLOv8, EasyOCR, Streamlit
    [Autres dépendances techniques si nécessaire]

# Installation Guide

Suivez ces étapes pour installer le projet :

1. Créer un environnement virtuel :
    ```sh
    python -m venv venv
    ```

2. Activer l'environnement virtuel:
    ```sh
    source venv/bin/activate
    ```

3. Installer les dépendances requises:
    ```sh
    pip install -r requirements.txt
    ```
4. Installation de Git LFS

- Installer Git LFS : Sur Ubuntu ou Debian, utilise la commande suivante :
    ``` sudo apt update
        sudo apt install git-lfs
    ```
- Initialiser Git LFS : Une fois installé, initialise Git LFS :
    ```git lfs install
    ```

# Usage
1.  Pour lancer l'application, suivez les étapes suivantes après l'installation :
     ```web_app/streamlit run app.py 
     ```
2. Configuration : Assurez-vous que les fichiers de configuration, tels que les chemins vers le modèle YOLOv8 et le répertoire d'images d'entrée, sont correctement configurés.


# Contribution

Les contributions sont les bienvenues.