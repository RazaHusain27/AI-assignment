# Smart Agricultural Assistant

A machine learning web app that recommends the most suitable crop to grow,
based on soil nutrients and weather conditions.Predicts the best crop to grow from soil nutrients (N, P, K), pH,
temperature, humidity and rainfall, using a Random Forest model.

## Live demo
https://ai-assignment-5aztxq7k2lp8ujus5efb9v.streamlit.app/

 # Domain 3
 AGRICULTURE

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


## Results
Evaluated on a stratified 80/20 split (440 test records):
| Accuracy | 0.9955 |
| Macro F1-score | 0.9955 |
