# Use a lightweight python image
FROM python:3.12-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else from the current directory to the container
COPY . .

# Ensure standard output is sent straight to terminal
ENV PYTHONUNBUFFERED=1

# Expose FastAPI port
EXPOSE 8000

# Run the FastAPI server via Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
