import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from preprocess import preprocess_data

# Create models directory if not exists
os.makedirs('models', exist_ok=True)

print("--- Step 1: Loading and Preprocessing Data ---")
df = preprocess_data('data/ipl_ball_by_ball.csv')

# Step 2: Feature-Target Split
X = df.drop('final_score', axis=1)
y = df['final_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create Pipeline (Matches app.py logic)
categorical_features = ['batting_team', 'bowling_team']
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)],
    remainder='passthrough'
)

model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42))
])

print("--- Step 2: Training the Pipeline ---")
model_pipeline.fit(X_train, y_train)

# --- CRITICAL FIX: Filename must match what app.py loads ---
MODEL_NAME = 'models/ipl_ultimate_model.pkl'
joblib.dump(model_pipeline, MODEL_NAME)
print(f"--- Step 3: SUCCESS! Model saved in {MODEL_NAME} ---")