import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI, UploadFile, File
from app.database import Base, engine
from app.models import prediction_model
from notebooks.HaarCascade import my_model_prediction
import aiofiles,uuid
import numpy as np

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def Home():
    return { "message" : "Hello from the another side !!"}

@app.post("/predictions")
async def create_predection(file : UploadFile = File(...)):
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
    return { "confidence" : confidence,
            "label" : label
            }

