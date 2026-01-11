# Toxic Comments Detector

Сервис для автоматического выявления токсичных комментариев на базе модели **DistilBERT**.  
Инференс реализован как REST API через **FastAPI**.

## Запуск

### 1) Установка зависимостей
```bash
pip install -r requirements.txt

### 2) Проверка наличия модели

models/distilbert-toxic/

### 3) Запуск API

uvicorn app.main:app --host 0.0.0.0 --port 8000


