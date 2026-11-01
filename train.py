import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# 1. Load data
df = pd.read_csv("data/Crop_recommendation.csv")
X = df[FEATURES]
y = df["label"]

# 2. Split: 80% train, 20% test (stratify keeps crop proportions equal)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate on data the model has never seen
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions), 4))
print(classification_report(y_test, predictions))

# 5. Save the model and the test set (for test_model.py)
joblib.dump(model, "crop_model.joblib")
test_data = X_test.copy()
test_data["label"] = y_test
test_data.to_csv("data/test_split.csv", index=False)
print("Saved: crop_model.joblib and data/test_split.csv")