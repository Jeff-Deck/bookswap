#!/bin/bash

# Levanta Django en segundo plano en el puerto 8000
gunicorn backend.wsgi:application --bind 0.0.0.0:8000 &

# Levanta FastAPI en el puerto 8001 
uvicorn api.main:app --host 0.0.0.0 --port 8001
