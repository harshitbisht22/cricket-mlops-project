from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import os

app = FastAPI(title="IPL Score Predictor Final")

# 1. Load the Pipeline (Preprocessor + Model)
MODEL_PATH = 'models/ipl_ultimate_model.pkl'

if os.path.exists(MODEL_PATH):
    # This loads the entire pipeline (OneHotEncoder + RandomForest)
    model_pipeline = joblib.load(MODEL_PATH)
    print(f"Successfully loaded {MODEL_PATH}")
else:
    print(f"ERROR: {MODEL_PATH} not found!")

class MatchInput(BaseModel):
    batting_team: str
    bowling_team: str
    overs: float
    current_score: int
    wickets_fallen: int

@app.get("/")
def home():
    return {"message": "IPL Predictor is Online"}

@app.post("/predict")
def predict_score(data: MatchInput):
    # Create DataFrame with EXACT column names used in training
    # The order must be exactly what the Pipeline expects
    input_df = pd.DataFrame([[
        data.batting_team, 
        data.bowling_team, 
        data.overs, 
        data.current_score, 
        data.wickets_fallen
    ]], columns=['batting_team', 'bowling_team', 'overs', 'current_score', 'wickets_fallen'])
    
    # Predict using the loaded pipeline
    prediction = model_pipeline.predict(input_df)[0]
    
    return {
        "predicted_score": int(prediction),
        "input_summary": data.dict()
    }