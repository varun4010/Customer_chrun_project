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

## 🚀 Getting Started

### Prerequisites
- **Python**: 3.9+ installed
- **Node.js**: 18+ and `npm` installed

---

### 1️⃣ Backend Setup (Django & ML Engine)

1. **Navigate to the project root**:
   ```bash
   cd customerChurnPred
   ```

2. **Create and activate a Python virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On macOS/Linux
   # venv\Scripts\activate     # On Windows
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   cd backend
   python manage.py migrate
   ```

5. **Train and Export the ML Model** *(Optional - Pre-trained model already saved)*:
   To retrain the XGBoost model with Optuna optimization:
   ```bash
   PYTHONPATH=. python ml_engine/train_and_save.py
   ```

6. **Start the Django backend server**:
   ```bash
   python manage.py runserver 8000
   ```
   The backend server will run at: `http://127.0.0.1:8000/`

---

### 2️⃣ Frontend Setup (React + Vite)

1. **Open a new terminal window** and navigate to the frontend directory:
   ```bash
   cd customerChurnPred/frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Start the Vite development server**:
   ```bash
   npm run dev
   ```
   The frontend application will run at: `http://localhost:5173/`

---

## 🔌 API Endpoints Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health/` | Server & model loaded health check |
| `POST` | `/api/predict/` | Predict churn probability for a single customer |
| `POST` | `/api/batch-predict/` | Predict churn for multiple customer records |
| `GET` | `/api/metadata/` | Fetch model performance metrics & threshold |
| `GET` | `/api/decision-boundary/` | Retrieve decision boundary curve points for visual analytics |

### Sample Single Prediction Request (`POST /api/predict/`)

```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Female",
  "Age": 42,
  "Tenure": 5,
  "Balance": 75000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 0,
  "EstimatedSalary": 105000.0,
  "SatisfactionScore": 3,
  "CardType": "DIAMOND",
  "PointEarned": 450
}
```

---

## 📜 License

This project is open-source and available under the **MIT License**.
