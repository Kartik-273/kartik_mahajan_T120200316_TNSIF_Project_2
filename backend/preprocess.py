import numpy as np

def preprocess_input(data: dict):
    """
    Converts dictionary input into numpy array for model.
    """
    features = np.array([[
        data['age'],
        data['sex'],
        data['chest_pain_type'],
        data['resting_blood_pressure'],
        data['cholesterol'],
        data['fasting_blood_sugar'],
        data['resting_ecg'],
        data['max_heart_rate'],
        data['exercise_induced_angina'],
        data['st_depression'],
        data['st_slope'],
        data['num_major_vessels'],
        data['thalassemia']
    ]], dtype=float)
    return features
