"""
API-Tests für die Diabetes Risk Prediction API
Ausführen mit: pytest tests/test_api.py -v
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ──────────────────────────────────────────
# Beispiel-Patienten
# ──────────────────────────────────────────
PATIENT_HIGH_RISK = {
    "age": 58, "sex": 0, "bmi": 38.5, "glucose": 195,
    "blood_pressure": 95, "insulin": 180, "skin_thickness": 35,
    "pregnancies": 3, "family_history": 1, "dpf": 1.2,
    "smoker": 1, "activity_level": 0
}

PATIENT_LOW_RISK = {
    "age": 28, "sex": 1, "bmi": 22.1, "glucose": 88,
    "blood_pressure": 68, "insulin": 40, "skin_thickness": 18,
    "pregnancies": 0, "family_history": 0, "dpf": 0.15,
    "smoker": 0, "activity_level": 2
}


# ──────────────────────────────────────────
# Tests
# ──────────────────────────────────────────
def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "api" in r.json()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_predict_high_risk():
    r = client.post("/predict", json=PATIENT_HIGH_RISK)
    assert r.status_code == 200
    data = r.json()
    assert data["risk_level"] in ["MITTEL", "HOCH"]
    assert 0 <= data["risk_probability"] <= 1
    assert len(data["top_risk_factors"]) > 0

def test_predict_low_risk():
    r = client.post("/predict", json=PATIENT_LOW_RISK)
    assert r.status_code == 200
    data = r.json()
    assert data["risk_level"] in ["NIEDRIG", "MITTEL"]

def test_predict_validation_error():
    r = client.post("/predict", json={"age": 200, "glucose": -10})
    assert r.status_code == 422  # Validation Error

def test_batch_predict():
    r = client.post("/predict/batch", json={"patients": [PATIENT_HIGH_RISK, PATIENT_LOW_RISK]})
    assert r.status_code == 200
    data = r.json()
    assert data["summary"]["total"] == 2
    assert len(data["predictions"]) == 2

def test_model_stats():
    r = client.get("/stats")
    assert r.status_code == 200
    assert "performance" in r.json()
    assert r.json()["performance"]["auc_roc"] > 0.9
