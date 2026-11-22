import joblib
import pandas as pd
import streamlit as st

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]


@st.cache_resource  # load the model once, not on every click
def load_model():
    return joblib.load("crop_model.joblib")


def confidence_level(percent):
    # Thresholds are my own simple choice, you can change them
    if percent >= 80:
        return "High"
    if percent >= 50:
        return "Medium"
    return "Low"


model = load_model()

st.title("🌾 Crop Recommendation")
st.write("Enter your soil and weather details to get a crop suggestion.")

col1, col2 = st.columns(2)
with col1:
    n = st.number_input("Nitrogen (N)", 0, 150, 90)
    p = st.number_input("Phosphorus (P)", 0, 150, 42)
    k = st.number_input("Potassium (K)", 0, 210, 43)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
with col2:
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 200.0)

if st.button("Predict crop"):
    input_data = pd.DataFrame(
        [[n, p, k, temperature, humidity, ph, rainfall]], columns=FEATURES
    )

    # One probability per crop; the highest one is the prediction
    probabilities = model.predict_proba(input_data)[0]
    best_index = probabilities.argmax()
    best_crop = model.classes_[best_index]
    confidence = probabilities[best_index] * 100

    st.success(f"Recommended crop: **{best_crop}**")

    # Confidence of the best prediction
    st.metric("Confidence", f"{confidence:.1f}%", confidence_level(confidence))
    st.progress(float(probabilities[best_index]))

    if confidence < 50:
        st.warning(
            "Low confidence: the model is unsure. Check your input values "
            "and compare with the other suggestions below."
        )

    # Top 3 choices with confidence
    top3 = sorted(zip(model.classes_, probabilities), key=lambda x: x[1], reverse=True)[:3]
    st.write("Top 3 suggestions:")
    for crop, prob in top3:
        st.write(f"- {crop}: {prob * 100:.1f}%")
