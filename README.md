# Manufacturing Parts Per Hour Predictor

## 🚀 Overview
Streamlit + PyTorch app that predicts machine productivity based on process parameters.

## 🧩 Structure
- **backend/** — model loading, preprocessing, and prediction utilities  
- **frontend/** — Streamlit UI form for inputs  
- **model/** — trained PyTorch `.pkl` from Colab  

## ▶️ Run
```bash
pip install -r requirements.txt
streamlit run frontend/app.py
