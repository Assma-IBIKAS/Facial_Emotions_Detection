import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from fastapi import FastAPI
from app.database import Base, engine
from app.models import prediction_model

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def Home():
    return { "message" : "Hello from the another side !!"}

