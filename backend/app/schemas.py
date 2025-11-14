from pydantic import BaseModel
from datetime import datetime

#* Schéma pour créer une nouvelle prédiction (input)
#* utilisé pour valider et insérer les données reçues par /predict_emotion dans la base de données
class PredictionCreate(BaseModel):
    emotion: str    # résultat du modèle
    confidence: float         # score de confiance (0.0 à 1.0)
    created_at: datetime