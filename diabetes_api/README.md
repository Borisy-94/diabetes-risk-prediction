# 🏥 Diabetes Risk Prediction API

FastAPI-basierte REST-API zur Echtzeit-Vorhersage des Diabetesrisikos.

## Schnellstart

```bash
# 1. Abhängigkeiten installieren
pip install -r requirements.txt

# 2. Modell aus dem Notebook exportieren (einmalig)
jupyter nbconvert --to script ../diabetes_risk_prediction.ipynb
python diabetes_risk_prediction.py

# 3. API starten
uvicorn app.main:app --reload --port 8000
```

## Endpoints

| Methode | Endpoint         | Beschreibung                        |
|---------|-----------------|-------------------------------------|
| GET     | `/`             | API-Info & Status                   |
| GET     | `/health`       | Health-Check                        |
| POST    | `/predict`      | Einzelvorhersage (1 Patient)        |
| POST    | `/predict/batch`| Batch-Vorhersage (bis 500 Patienten)|
| GET     | `/stats`        | Modell-Performance-Metriken         |
| GET     | `/docs`         | Swagger UI (interaktiv testen)      |

## Beispiel-Anfrage

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45, "sex": 0, "bmi": 31.2,
    "glucose": 148, "blood_pressure": 82,
    "insulin": 120, "skin_thickness": 28,
    "pregnancies": 2, "family_history": 1,
    "dpf": 0.627, "smoker": 0, "activity_level": 1
  }'
```

## Beispiel-Antwort

```json
{
  "patient_id": "PAT-1423589",
  "risk_probability": 0.7341,
  "risk_level": "HOCH",
  "risk_score": 6.5,
  "recommendation": "⚠️ Sofortige ärztliche Konsultation empfohlen.",
  "top_risk_factors": [
    "Erhöhter Glukosewert (148 mg/dL > 126)",
    "Fettleibigkeit (BMI 31.2 ≥ 30)",
    "Positive Familienhistorie für Diabetes"
  ]
}
```

## Power BI Integration

Die Batch-API (`/predict/batch`) kann direkt als Web-Datenquelle in Power BI eingebunden werden:
1. Power BI → Daten abrufen → Web
2. URL: `http://localhost:8000/predict/batch`
3. Methode: POST mit JSON-Body

## Tests ausführen

```bash
pytest tests/test_api.py -v
```
