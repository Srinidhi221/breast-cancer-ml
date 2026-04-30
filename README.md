# breast-cancer-ml

# 🧬 Breast Cancer Classification using Machine Learning

## 📌 Overview

This project builds a machine learning model to classify breast tumors as **Benign (B)** or **Malignant (M)** using clinical features.
The goal is to assist early detection by analyzing tumor characteristics and predicting the likelihood of cancer.

---

## 📊 Dataset

* Source: Breast Cancer Wisconsin Dataset
* Samples: 569
* Features: 30 numerical attributes (radius, texture, perimeter, area, etc.)
* Target: Diagnosis (Benign / Malignant)

---

## 🧠 Project Workflow

1. Data Loading & Exploration
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Model Training
5. Model Evaluation
6. Model Comparison
7. Threshold Tuning
8. Model Saving

---

## ⚙️ Models Used

* Logistic Regression
* Decision Tree

---

## 📈 Evaluation Metrics

* Accuracy
* Precision & Recall
* F1 Score
* ROC Curve & AUC
* Confusion Matrix
* Cross-Validation (K-Fold)

---

## 📊 Results Summary

| Metric         | Logistic Regression | Decision Tree |
| -------------- | ------------------- | ------------- |
| Accuracy       | ~96%                | ~92%          |
| AUC Score      | ~0.99               | ~0.95         |
| Stability (CV) | High                | Moderate      |

---

## 🔍 Key Insights

* Logistic Regression outperformed Decision Tree across all metrics
* Tumor size and shape features (radius, perimeter, concavity) are highly predictive
* Lowering classification threshold reduces **False Negatives**, which is critical in medical diagnosis

---

## 💾 Model Saving

Trained models and preprocessing steps are saved using `joblib` for reuse without retraining.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone [(https://github.com/Srinidhi221/breast-cancer-ml.git)]
cd breast-cancer-ml
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run notebook

Open `notebooks/analysis.ipynb` in Jupyter/Colab

---

## 📁 Project Structure

```
breast-cancer-ml/
│
├── data/
├── notebooks/
│   └── analysis.ipynb
├── saved_models/
├── src/
├── README.md
└── requirements.txt
```

---

## 🌐 Deployment (Optional)

The model can be deployed using a simple Flask API for real-time predictions.

---

## 🌐 Live API
https://your-app-name.onrender.com
Note: API may take ~30–50 seconds on first request due to free-tier cold start.

## 🔮 Future Improvements

* Implement Random Forest / XGBoost
* Add feature selection techniques
* Deploy a user-friendly web interface
* Integrate explainability tools (e.g., SHAP)

---

## 🎯 Conclusion

This project demonstrates a complete machine learning workflow from data analysis to model deployment, with a focus on real-world medical relevance and interpretability.

---

## 📬 Contact

For queries or collaboration, feel free to connect.

---
