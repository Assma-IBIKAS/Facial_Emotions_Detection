# 🧠 Facial Emotion Detection API

API d'analyse émotionnelle à partir d'images faciales --- Détection de
visage, prédiction d'émotion via CNN, et stockage des prédictions en
base PostgreSQL.

## 🎯 Contexte du projet

Ce projet a été réalisé dans le cadre du développement d’un prototype d’API IA pour l’analyse émotionnelle à partir d’images faciales.
L’objectif est d’évaluer la faisabilité d’un futur produit SaaS capable de mesurer les réactions des utilisateurs lors de tests produits ou de sessions UX.

L’API doit permettre de :

📸 détecter automatiquement un visage dans une image,

😀 prédire l’émotion (happy, sad, angry, neutral, etc.),

🗄️ enregistrer la prédiction dans une base PostgreSQL,

🔄 fournir un historique d’utilisation.

## 📥 Fonctionnalités demandées

-   Upload d'image via POST\
-   Détection du visage (OpenCV + Haar Cascade)\
-   Prédiction via modèle CNN TensorFlow\
-   Sauvegarde en base PostgreSQL : id, emotion, confidence, created_at

# 1️⃣ Préparation des données

Dataset structure :

    dataset/
     ├── angry/
     ├── disgusted/
     ├── fearful/
     ├── happy/
     ├── neutral/
     ├── sad/
     └── surprised/

Chargement via :

``` python
tf.keras.utils.image_dataset_from_directory()
```

# 2️⃣ Entraînement du modèle CNN

Prétraitements : - normalisation - Batch Normalization

Architecture : - Conv2D, MaxPooling2D, Flatten, Dense, Dropout

Optimisation : - Adam + categorical_crossentropy

Sauvegarde :

``` python
model.save("my_modele.h5")
```

# 3️⃣ Détection de visages (OpenCV)

``` python
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = facecascade.detectMultiScale(gray_img, 1.3, 5)
```

Script : `detect_and_predict.py`\
→ détection + prédiction + affichage rectangle + label

# 4️⃣ API FastAPI

## POST /predict_emotion

-   reçoit une image
-   détecte le visage
-   prédit émotion
-   retourne JSON :

``` json
{
  "emotion": "happy",
  "confidence": 0.98
}
```

-   enregistre dans PostgreSQL

## GET /history

Retourne l'historique :

``` json
[
  {
    "id": 1,
    "emotion": "sad",
    "confidence": 0.74,
    "created_at": "2025-02-14T10:22:40"
  }
]
```

# 5️⃣ Tests unitaires

-   test chargement modèle\
-   test du format de /history

# 🤖 GitHub Actions

Pipeline CI : - installation dépendances\
- exécution de pytest

# 📦 Structure du projet

    project/
     ├── backend/
     ├── notebooks/
        ├── detect_and_predict.py
     ├── tests/
     ├── requirements.txt
     └── README.md

# 🛠️ Technologies

Python, FastAPI, TensorFlow, OpenCV, SQLAlchemy, PostgreSQL, Pytest,
GitHub Actions

# 🎉 Conclusion

Pipeline IA complet : préparation → CNN → détection → API → base de
données → tests CI.
