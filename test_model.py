import joblib
import pandas as pd

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Test 1: the model file loads
model = joblib.load("crop_model.joblib")
print("PASS: model loaded")

# Test 2: a single prediction returns a crop name
sample = pd.DataFrame(
    [[90, 42, 43, 20.9, 82.0, 6.5, 202.9]], columns=FEATURES
)
result = model.predict(sample)[0]
assert isinstance(result, str), "Prediction should be a crop name"
print("PASS: single prediction ->", result)

# Test 3: accuracy on the held-out test set is good enough
test_data = pd.read_csv("data/test_split.csv")
accuracy = (model.predict(test_data[FEATURES]) == test_data["label"]).mean()
assert accuracy > 0.90, f"Accuracy too low: {accuracy:.2f}"
print(f"PASS: test accuracy = {accuracy:.4f}")

print("\nAll tests passed.")