import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, roc_auc_score
import pickle

# 🔹 Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 🔹 Preprocessing
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# 🔹 Convert target
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# 🔹 Create REAL features (not random)

# Ticket-like behavior derived from tenure
df["freq_90"] = (df["tenure"] // 3).astype(int)
df["freq_30"] = (df["tenure"] // 6).astype(int)
df["freq_7"] = (df["tenure"] // 12).astype(int)

# Avg gap (inverse of frequency)
df["avg_gap"] = (df["tenure"] + 1) / (df["freq_30"] + 1)

# Charges increase (based on charges vs median)
df["charges_increase"] = (df["MonthlyCharges"] > df["MonthlyCharges"].median()).astype(int)

# 🔹 Features (match API exactly)
X = df[["freq_7", "freq_30", "freq_90", "avg_gap", "charges_increase"]]
y = df["Churn"]

# 🔹 Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Train model
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# 🔹 Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# 🔹 Metrics
print("F1 Score:", f1_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# 🔹 Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

