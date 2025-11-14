
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI, UploadFile, File,Depends
from app.database import Base, engine, get_db
from app.models import prediction_model
from notebooks.HaarCascade import my_model_prediction
import aiofiles,uuid
import numpy as np
from sqlalchemy.orm import Session
from app.models.prediction_model import Prediction

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def Home():
    return { "message" : "Hello from the another side !!"}

@app.post("/predictions")
async def create_predection(file : UploadFile = File(...), database : Session = Depends(get_db)):

    file_ext = file.filename.split(".")[-1]
    temp_filename = f"{uuid.uuid4()}.{file_ext}"

    async with aiofiles.open(temp_filename, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
    confidence,label = my_model_prediction(temp_filename)
    # Convertir numpy.float32 ou Tensor en float natif Python
    if isinstance(confidence, (np.ndarray, np.generic)):
        confidence = float(confidence)
    elif hasattr(confidence, "numpy"):  # si TensorFlow tensor
        confidence = float(confidence.numpy())

    db_pred = Prediction(
        emotion = label,
        confidence = confidence
    )

    database.add(db_pred)
    database.commit()
    database.refresh(db_pred)

    return { "confidence" : db_pred.confidence,
            "label" : db_pred.emotion
            }

@app.get("/History")
def get_history(database : Session = Depends(get_db)):

    preds = database.query(Prediction).order_by(Prediction.created_at.desc()).all()

    results = []
    for pred in preds:
        results.append({
            "id" : pred.id,
            "emotion" : pred.emotion,
            "confidence" : round(pred.confidence,2),
            "date" : pred.created_at.strftime("%d/%m/%Y %H:%M:%S")
        })

    return results



