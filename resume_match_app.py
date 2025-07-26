
import streamlit as st
import joblib

st.title("🧠 Resume Job Matcher")
st.write("Enter your resume summary or skills to see the best job match.")

input_text = st.text_area("Your Resume Summary:")

if input_text:
    model = joblib.load("models/resume_model.joblib")
    vectorizer = joblib.load("models/resume_vectorizer.joblib")
    vec = vectorizer.transform([input_text])
    prediction = model.predict(vec)[0]
    st.success(f"✅ Predicted Job Role: **{prediction}**")
