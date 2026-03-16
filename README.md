# 🏏 IPL Score Predictor (MLOps Project)

An **end-to-end Machine Learning + MLOps project** that predicts the **first-innings score of an IPL match** using real-time match data.

The model is exposed via a **FastAPI REST API**, containerized with **Docker**, and prepared for **Kubernetes deployment**.

---

# 🚀 Project Overview

This project demonstrates how to take a Machine Learning model from **training → API → container → production-ready deployment**.

### 🔹 Model
- **Algorithm:** Random Forest Regressor
- **Training Data:** Historical IPL ball-by-ball dataset
- **Output:** Predicted first innings score

### 🔹 API Layer
- **Framework:** FastAPI
- **Features**
  - High performance async API
  - Automatic Swagger documentation
  - Input validation using Pydantic

### 🔹 Containerization
- **Docker**
- **Base Image:** `python:3.12-slim`

### 🔹 Deployment Ready
- Kubernetes manifests can be added to deploy the service on a cluster.

---

# 🛠️ Running the Project

## 1️⃣ Run Using Docker (Recommended)

Pull the image from Docker Hub and run the container.

```bash
docker pull harshitbisht/cricket-predictor:latest

docker run -p 8000:8000 harshitbisht/cricket-predictor:latest

The API will start at:

http://localhost:8000
2️⃣ Run Manually (Without Docker)
Install dependencies
pip install -r requirements.txt
Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000
📊 API Documentation

Once the server is running, you can access the API documentation:

Swagger UI
http://localhost:8000/docs
ReDoc Documentation
http://localhost:8000/redoc
📥 Sample Prediction Request

Example JSON request:

{
  "batting_team": "Royal Challengers Bangalore",
  "bowling_team": "Kolkata Knight Riders",
  "overs": 15.2,
  "current_score": 145,
  "wickets_fallen": 3
}

The API will return the predicted final score for the first innings.

📁 Project Structure
.
├── main.py              # FastAPI application
├── pipe.pkl             # Serialized ML pipeline (model + preprocessing)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container configuration
├── .gitignore           # Ignore unnecessary files
└── README.md            # Project documentation
🧠 Tech Stack

Python

Scikit-learn

FastAPI

Docker

Kubernetes (for deployment)

📦 Docker Image

Available on Docker Hub:

harshitbisht/cricket-predictor

Pull command:

docker pull harshitbisht/cricket-predictor:latest
🔮 Future Improvements

Add CI/CD pipeline (GitHub Actions)

Deploy on Kubernetes (EKS / Minikube)

Add Prometheus + Grafana monitoring

Add ML model versioning

Integrate MLflow for experiment tracking

👨‍💻 Author

Harshit Bisht

DevOps | Cloud | Kubernetes | MLOps

LinkedIn:
https://www.linkedin.com/in/harshit-bisht-0a0a69148/