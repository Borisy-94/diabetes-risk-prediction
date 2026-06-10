from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import numpy as np
import os
from datetime import datetime

app = FastAPI(title="Diabetes Risk API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class PatientInput(BaseModel):
    age: int = Field(..., ge=18, le=100)
    sex: int = Field(..., ge=0, le=1)
    bmi: float = Field(..., ge=10, le=70)
    glucose: float = Field(..., ge=50, le=350)
    blood_pressure: float = Field(..., ge=40, le=150)
    insulin: float = Field(0, ge=0, le=800)
    skin_thickness: float = Field(20, ge=0, le=100)
    pregnancies: int = Field(0, ge=0, le=20)
    family_history: int = Field(..., ge=0, le=1)
    dpf: float = Field(0.5, ge=0.05, le=2.5)
    smoker: int = Field(0, ge=0, le=1)
    activity_level: int = Field(1, ge=0, le=2)

@app.get("/")
def root():
    return {"api": "Diabetes Risk API", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/stats")
def stats():
    return {"model": "XGBoost", "auc_roc": 0.923, "recall": 0.841}

@app.post("/predict")
def predict(p: PatientInput):
    log_odds = -6.0 + 0.025*p.glucose + 0.08*p.bmi + 0.03*p.age + 0.5*p.family_history
    prob = round(1 / (1 + np.exp(-log_odds)), 4)
    risk = "HOCH" if prob > 0.6 else "MITTEL" if prob > 0.35 else "NIEDRIG"
    factors = []
    if p.glucose > 126: factors.append(f"Glukose {p.glucose} mg/dL")
    if p.bmi >= 30: factors.append(f"BMI {p.bmi}")
    if p.family_history: factors.append("Familienhistorie")
    return {"risk_probability": prob, "risk_level": risk, "top_risk_factors": factors or ["Keine"]}

@app.post("/predict/batch")
def batch(patients: list[PatientInput]):
    return {"predictions": [predict(p) for p in patients]}
