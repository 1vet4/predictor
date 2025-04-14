# Predictor application

This repository contains a simple application to predict GPD per capita using a Random Forest Classifier trained on official GDP data.

## Python version 3.15.*

# Docker image setup

1. Create Dockerfile 

FROM python:3.11-slim    # specify base image

ENV PYTHONDONTWRITEBYTECODE 1   # ensures that Python will not generate .pyc files which keeps the container smaller
ENV PYTHONUNBUFFERED 1

WORKDIR /api        # set working directory

COPY requirements.txt /api/    # copy requirement.txt into /api

RUN pip install --upgrade pip && pip install -r requirements.txt       # install dependencies inside container

EXPOSE 8033     # expose port for network traffic
COPY . /api/    # copy rest of application into /api

CMD ["gunicorn", "--workers=3", "--bind=:8033", "--preload", "--threads=20", "run_api:app"]

2. to build the image run: docker build -t predictor .
3. to start the container run: docker run -p 8033:8033 predictor
4. to confirm the container is running: docker ps
   CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                    NAMES
d40a2141abb2   predictor   "gunicorn --workers=…"   3 minutes ago   Up 3 minutes   0.0.0.0:8033->8033/tcp   quizzical_gagarin
5. testing the application on localhost:8033 confirms that the code is running correctly
6. to stop the container run: docker stop d40a2141abb2
