import pickle
import numpy as np
import os
import sys

# ✅ Dynamically add backend/utils to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

# Now safe to import preprocess_input
from preprocess import preprocess_input

# === Load trained model ===
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'iteration2_model.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_heart_disease(data: dict):
    features = preprocess_input(data)
    prediction = model.predict(features)[0]
    return prediction
