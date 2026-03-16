🏏 IPL Score Predictor (MLOps)
This is an end-to-end Machine Learning project that predicts the first-innings score of an IPL match based on real-time match data. The project is production-ready, served via FastAPI, and fully Dockerized.

🚀 Project Overview
Model: Random Forest Regressor trained on historical IPL ball-by-ball data.

API Framework: FastAPI (with automated Swagger documentation).

Containerization: Docker (Python 3.12-slim base image).

Deployment Ready: Manifests included for Kubernetes orchestration.

🛠️ How to Run Locally
1. Using Docker (Recommended)
You can pull the pre-built image directly from Docker Hub:

Bash
docker pull harshitbisht/cricket-predictor:latest
docker run -p 8000:8000 harshitbisht/cricket-predictor:latest
2. Manual Setup
Bash
# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8000
📊 API Documentation
Once the server is running, visit:

Interactive Docs: http://localhost:8000/docs

JSON Schema: http://localhost:8000/redoc

Sample Request (JSON)
JSON
{
  "batting_team": "Royal Challengers Bangalore",
  "bowling_team": "Kolkata Knight Riders",
  "overs": 15.2,
  "current_score": 145,
  "wickets_fallen": 3
}
📁 Project Structure
main.py: The FastAPI application.

pipe.pkl: The serialized ML pipeline (Model + Preprocessor).

Dockerfile: Instructions for containerizing the app.

.gitignore: Prevents heavy data files and venv from being uploaded.