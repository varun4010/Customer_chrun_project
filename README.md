# 📊 Customer Churn Prediction System

An end-to-end Machine Learning web application designed to predict bank customer churn, evaluate churn risk probability, analyze key feature drivers, and perform interactive scenario testing. Built with a **Django REST API** backend and a modern **React + Vite** frontend.

---

## 🌟 Features

- 🤖 **Advanced ML Engine**: Hyperparameter-tuned **XGBoost Classifier** optimized via **Optuna** and Scikit-Learn pipelines.
- ⚡ **Singleton Preloading Engine**: Preloads serialized model weights (`.joblib`) into memory at Django startup for sub-millisecond API response times.
- 🎨 **Interactive React Frontend**: Responsive dashboard featuring:
  - **Single Customer Prediction**: Form inputs for demographic & banking details with instant risk gauge visualization.
  - **Batch Predictions**: Upload customer datasets (CSV/JSON) for batch churn evaluation.
  - **Scenario Simulator ("What-If" Analysis)**: Adjust customer attributes dynamically to see real-time shifts in churn probability.
  - **Decision Boundary & Feature Importance**: Visual insights into model decision thresholds, precision-recall metrics, and top predictive drivers.
- 🛡️ **Data Validation**: Strict input validation using Django REST Framework Serializers.

---

## 🛠️ Tech Stack

### **Backend & Machine Learning**
- **Framework**: Django 4.x / 5.x, Django REST Framework (DRF)
- **CORS**: `django-cors-headers`
- **Machine Learning**: Scikit-Learn, XGBoost, Optuna (TPE Sampler)
- **Data Engineering**: Pandas, NumPy, Joblib, KaggleHub

### **Frontend**
- **UI Framework**: React 19 (JavaScript / ES Modules)
- **Build Tool**: Vite
- **Styling & Animations**: Vanilla CSS with modern Glassmorphism & Framer Motion
- **Data Visualization**: Recharts
- **Icons & Effects**: Lucide React, Canvas Confetti

---

## 📁 Directory Structure

```text
customerChurnPred/
├── backend/
│   ├── churn_project_backend/  # Django settings, WSGI/ASGI configuration & root URLs
│   ├── api_backend/            # REST API app (views, serializers, model loader, services)
│   ├── ml_engine/              # Training pipeline scripts & feature engineering
│   │   ├── feature_engineering.py  # Domain-specific feature transformation functions
│   │   ├── train_and_save.py       # Optuna hyperparameter tuning & XGBoost training script
│   │   └── saved_models/           # Exported .joblib pipeline, metadata.json, decision_boundary.json
│   ├── manage.py               # Django management entrypoint
│   └── db.sqlite3              # SQLite Database
├── frontend/
│   ├── src/                    # React components, pages, and API client integration
│   ├── index.html              # Vite entrypoint HTML
│   ├── package.json            # Node.js dependencies & scripts
│   └── vite.config.js          # Vite developer configuration
├── requirements.txt            # Python backend dependencies
└── README.md                   # Project documentation
```

---









