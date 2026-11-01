# Smart Agricultural Assistant

Predicts the best crop to grow from soil nutrients (N, P, K), pH,
temperature, humidity and rainfall, using a Random Forest model.

## Files
- train.py: trains the model and saves crop_model.joblib
- test_model.py: checks the saved model works
- app.py: Streamlit web app

## Run locally
pip install -r requirements.txt
python train.py
python test_model.py
python -m streamlit run app.py

## Dataset
Crop Recommendation Dataset from Kaggle.

## Live demo
https://ai-assignment-5aztxq7k2lp8ujus5efb9v.streamlit.app/
