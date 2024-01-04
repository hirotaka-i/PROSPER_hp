# app/Dockerfile
FROM python:3.9.6

WORKDIR /app

EXPOSE 8080
COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt
COPY data data
COPY *.py ./
COPY prosper1-firebase-adminsdk-w1jxl-33a055c618.json prosper1-firebase-adminsdk-w1jxl-33a055c618.json

# Run the application
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]