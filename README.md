🏥 Predictive Diabetes Analytics
Power BI Dashboard

📋 Projektübersicht
Dieses Projekt demonstriert eine vollständige End-to-End Machine Learning Pipeline zur Früherkennung von Diabetes-Risikopatienten — von der Datengenerierung über das Modelltraining bis hin zur Echtzeit-API und einem interaktiven Power BI Dashboard.

Hintergrund: Als ausgebildeter biomedizinischer Laboranalytiker kombiniere ich mein klinisches Wissen mit Data Analytics, um aus Patientendaten actionable Insights zu gewinnen — von der individuellen Laboranalyse zur bevölkerungsweiten Risikoerkennung.


🎯 Projektziele

Diabetes-Risiko aus klinischen Patientendaten vorhersagen
ML-Modell als REST API in Echtzeit deployen
Ergebnisse in einem interaktiven Dashboard visualisieren
Modell-Entscheidungen mit SHAP transparent machen


🏗️ Architektur
📁 Datengenerierung (Python/Faker)
    ↓
📊 Explorative Datenanalyse (EDA)
    ↓
🧠 Feature Engineering + ML-Training (XGBoost)
    ↓
📡 REST API Deployment (FastAPI)
    ↓
📈 Dashboard Visualisierung (Power BI)

📊 Ergebnisse
ModellAUC-ROCRecallPräzisionF1-ScoreLogistic Regression0.8510.7830.7200.750Random Forest0.9020.8140.7600.786XGBoost ✅0.9230.8410.7840.811
Top Risikofaktoren (SHAP)

🔴 Glukose — stärkster Prädiktor (SHAP: 0.92)
🟠 BMI — zweiter Hauptfaktor (SHAP: 0.74)
🟡 Alter — Risiko steigt ab 50 (SHAP: 0.58)
🟢 Familienhistorie — genetische Komponente (SHAP: 0.45)
🔵 Insulin — metabolischer Indikator (SHAP: 0.31)


🛠️ Tech Stack
KategorieTechnologieSprachePython 3.14MLXGBoost, scikit-learn, SHAPDatengenerierungFaker, NumPy, PandasAPIFastAPI, Uvicorn, PydanticVisualisierungPower BI, Matplotlib, SeabornVersionierungGit, GitHub

📁 Projektstruktur
diabetes-risk-prediction/
│
├── 📓 diabetes_risk_prediction.ipynb   # Haupt-Notebook (EDA + ML)
│
├── 📡 diabetes_api/
│   ├── app/
│   │   └── main.py                     # FastAPI Endpoints
│   ├── tests/
│   │   └── test_api.py                 # Unit Tests
│   ├── requirements.txt
│   └── README.md
│
├── 📊 dashboard/
│   └── Diabetes_Risk_Dashboard.pbix    # Power BI Dashboard
│
├── 📂 data/
│   ├── predictions_for_powerbi.csv     # Modell-Vorhersagen
│   └── shap_importance.csv             # SHAP Feature Importance
│
├── 📈 outputs/
│   ├── eda_distributions.png           # EDA Visualisierungen
│   ├── correlation_matrix.png          # Korrelationsmatrix
│   ├── model_evaluation.png            # ROC + Confusion Matrix
│   └── shap_beeswarm.png              # SHAP Beeswarm Plot
│
└── 🧠 models/
    ├── diabetes_xgboost_model.pkl      # Trainiertes Modell
    └── feature_config.json             # Feature Konfiguration

🚀 Schnellstart
1. Repository klonen
bashgit clone https://github.com/DEIN_USERNAME/diabetes-risk-prediction.git
cd diabetes-risk-prediction
2. Abhängigkeiten installieren
bashpip install -r diabetes_api/requirements.txt
pip install jupyter notebook xgboost shap faker matplotlib seaborn
3. Notebook ausführen
bashjupyter notebook diabetes_risk_prediction.ipynb
# Kernel → Restart & Run All
4. API starten
bashcd diabetes_api
uvicorn app.main:app --port 8000
5. API testen
http://localhost:8000/docs  ← Swagger UI

📡 API Endpoints
MethodEndpointBeschreibungGET/API StatusGET/healthHealth CheckGET/statsModell-MetrikenPOST/predictEinzelvorhersagePOST/predict/batchBatch-Vorhersage
Beispiel-Anfrage
bashcurl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45, "sex": 0, "bmi": 31.2,
    "glucose": 148, "blood_pressure": 82,
    "insulin": 120, "skin_thickness": 28,
    "pregnancies": 2, "family_history": 1,
    "dpf": 0.627, "smoker": 0, "activity_level": 1
  }'
Beispiel-Antwort
json{
  "risk_probability": 0.7341,
  "risk_level": "Hoch",
  "top_risk_factors": [
    "Erhöhter Glukosewert (148 mg/dL)",
    "Fettleibigkeit (BMI 31.2)",
    "Positive Familienhistorie"
  ]
}

👨‍💻 Über den Autor
Boris Petamba — Junior Data Analyst | Hamm, NRW
Biomedizinischer Laboranalytiker mit IHK-zertifizierter Data Analytics Ausbildung. Spezialisierung auf Healthcare Analytics und ML-Anwendungen im medizinischen Bereich.
Bild anzeigen

📄 Lizenz
MIT License — frei verwendbar für Lern- und Portfolio-Zwecke.
