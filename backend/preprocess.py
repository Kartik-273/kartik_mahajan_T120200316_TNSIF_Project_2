import numpy as np
import pandas as pd

def preprocess_input(input_dict, feature_columns):
    """
    Takes a dict from frontend form inputs and returns a numpy array (1, n_features)
    matching the model’s expected feature order.
    """
    df = pd.DataFrame([input_dict])
    df = df[feature_columns]  # ensure same order
    # Convert to float32 for PyTorch
    return df.values.astype(np.float32)
