import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


# Charger le modèle
model = load_model('notebooks/my_modele.h5')

# Les classes que ton modèle peut prédire
class_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def my_model_prediction(url_img):
    image = cv2.imread(url_img)
    print("Dimensions de l'image: ",image.shape)


    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # on charge notre modèle
    face_cascade = cv2.CascadeClassifier('notebooks/haarcascade.xml')

    # on verifie que le modèle a bien été chargée
    if face_cascade.empty()==True:
        print("Le fichier n'est pas chargé: ", face_cascade.empty())
    else:
        print("Le fichier est chargé.")


    #  On cherche tous les visages disponibles dans l'image
    faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=10)
    # on écrit dans la console le nombre de visages que  l'algorithme a détecté
    print(f"{len(faces)} visages detectés dans l'image.")


    for (x, y, w, h) in faces:
        # Extraire le visage en gris
        roi_gray = image_gray[y:y+h, x:x+w]
        
        # Redimensionner à la taille attendue par ton modèle (ex: 48x48)
        roi_gray = cv2.resize(roi_gray, (48, 48))
        
        # Normaliser et convertir en tableau
        roi = roi_gray.astype('float') / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)  

        # Prédiction
        preds = model.predict(roi)[0]
        label = class_labels[np.argmax(preds)]
        predicted_index = np.argmax(preds)
        label = class_labels[predicted_index]
        confidence = preds[predicted_index] * 100 
        
        # Afficher la prédiction et la probabilité sur l'image
        text = f"{label} ({confidence:.2f}%)"
        cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Afficher la prédiction sur l'image
        cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)


        # Afficher le résultat avec matplotlib
    # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # plt.figure(figsize=(8, 6))
    # plt.imshow(image)
    # plt.axis('off')
    # plt.show()

    return confidence,label