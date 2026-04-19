import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score, precision_recall_curve

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("data/telco.csv")

# Example preprocessing (modify based on your dataset)
df = df.dropna()

# Convert target
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# -------------------------------
# Feature Engineering
# -------------------------------
# Simulated features (since ticket logs are not in dataset)

df['ticket_7d'] = np.random.randint(0, 5, len(df))
df['ticket_30d'] = np.random.randint(0, 10, len(df))
df['ticket_90d'] = np.random.randint(0, 20, len(df))
df['sentiment'] = np.random.uniform(-1, 1, len(df))
df['monthly_change'] = np.random.uniform(-20, 20, len(df))

features = [
    'MonthlyCharges',
    'tenure',
    'ticket_7d',
    'ticket_30d',
    'ticket_90d',
    'sentiment',
    'monthly_change'
]

X = df[features]
y = df['Churn']

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Pipeline (IMPORTANT for MLOps)
# -------------------------------
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(n_estimators=100))
])

# Train
pipeline.fit(X_train, y_train)

# -------------------------------
# Evaluation
# -------------------------------
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# -------------------------------
# Save Model
# -------------------------------
joblib.dump(pipeline, "model/model.pkl")

print("Model saved successfully!")