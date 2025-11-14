import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from backend.main import app
from tensorflow.keras.models import load_model

client = TestClient(app)

def test_model_load():
    model = load_model("./notebooks/my_modele.h5")
    assert model is not None

def test_format():
    res = client.get("/History")            #? Envoyer une requête GET à l'endpoint /history | r contient la réponse de ton endpoint.
    assert res.status_code == 200, f"Status code incorrect: {res.status_code}"
    data = res.json()                       #? Transforme la réponse en JSON (r.json()) et vérifie que c'est une liste.
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    if data:  # Si la liste n'est pas vide
        pred = data[0]
        required_keys = ["id","emotion", "confidence", "date"]
        for key in required_keys:
            assert key in pred, f"Missing key: {key}"