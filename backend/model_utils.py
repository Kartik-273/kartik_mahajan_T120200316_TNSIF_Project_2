import os
import pickle
import torch
import torch.nn as nn
import numpy as np
from backend.preprocess import preprocess_input

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "iteration1_model.pkl")

class LinearRegressionModel(nn.Module):
    def __init__(self, in_features, out_features=1):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
    def forward(self, x):
        return self.linear(x)

def load_model():
    with open(MODEL_PATH, "rb") as f:
        saved = pickle.load(f)

    input_dim = saved["input_dim"]
    model = LinearRegressionModel(input_dim)
    model.load_state_dict(saved["model_state_dict"])
    model.eval()

    return model, saved["x_scaler"], saved["y_scaler"], saved["columns"], saved["target_name"]

# global lazy load
_model = None
_x_scaler = None
_y_scaler = None
_columns = None
_target_name = None

def get_model():
    global _model, _x_scaler, _y_scaler, _columns, _target_name
    if _model is None:
        _model, _x_scaler, _y_scaler, _columns, _target_name = load_model()
    return _model, _x_scaler, _y_scaler, _columns, _target_name

def predict(input_dict):
    """
    input_dict: {feature_name: value, ...}
    Returns predicted target value (float)
    """
    model, x_scaler, y_scaler, columns, target_name = get_model()

    X = preprocess_input(input_dict, columns)
    X_scaled = x_scaler.transform(X)
    X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
    with torch.no_grad():
        y_scaled_pred = model(X_tensor).numpy()
    y_pred = y_scaler.inverse_transform(y_scaled_pred.reshape(-1, 1))
    return float(y_pred[0, 0])

