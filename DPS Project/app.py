import streamlit as st
import joblib
from utils.feature_extraction import extract_features

# Load model
model = joblib.load("model/phishing_model.pkl")

st.title("🔐 Phishing Website Detector")
url_input = st.text_input("Enter the URL to check:")

if st.button("Check"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict([features])[0]

        if prediction == 1:
            st.error("⚠️ Warning: This website is likely a phishing site!")
        else:
            st.success("✅ This website seems to be safe.")
    else:
        st.warning("Please enter a URL.")
