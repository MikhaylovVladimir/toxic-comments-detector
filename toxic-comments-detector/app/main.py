from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "models/distilbert-toxic"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

app = FastAPI(title="Toxic Comments Detector")

class TextRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    text: str
    toxic_probability: float
    prediction: int

@app.post("/predict", response_model=PredictionResponse)
def predict(request: TextRequest):
    inputs = tokenizer(
        request.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=256,
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)

    prob_toxic = probs[0, 1].item()
    pred = int(prob_toxic >= 0.5)

    return {
        "text": request.text,
        "toxic_probability": prob_toxic,
        "prediction": pred,
    }
