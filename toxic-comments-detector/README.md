# Toxic Comments Detector

Сервис для автоматического выявления токсичных комментариев на базе модели **DistilBERT**.  
Инференс реализован как REST API через **FastAPI**.

Для работоспособности модели необходимо загрзуить в папку models/distilbert-toxic файл model.safetensors (из-за объема файла загрузить его на Гитхаб невозможно, поэтому он доступен на гугл диске по ссылке):

https://drive.google.com/file/d/1EDT58z4ap_6rkmkvFb1QvR2OPcU8OHHj/view?usp=sharing

## Запуск

### 1) Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2) Проверка наличия модели
```bash
models/distilbert-toxic/
```
### 3) Запуск API
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
### 4) Интерактивная проверка по адрессу
Svager UI
```bash
[uvicorn app.main:app --host 0.0.0.0 --port 8000](http://localhost:8000/docs
)
```

