import streamlit as st
import pickle
import pandas as pd


# Load the trained model
with open(r'c:/Users/User/learnML/Heart-Disease-Prediction/heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Heart Disease Prediction App")

st.sidebar.header("Input Patient Data")

def user_input():
    age = st.sidebar.number_input("Age", 1, 120, 60)
    sex = st.sidebar.selectbox("Sex", [0, 1])
    cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.sidebar.number_input("Resting BP", 80, 200, 120)
    chol = st.sidebar.number_input("Cholesterol", 100, 600, 200)
    fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.sidebar.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.sidebar.number_input("Max Heart Rate Achieved", 60, 250, 150)
    exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.sidebar.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
    slope = st.sidebar.selectbox("Slope of ST Segment", [0, 1, 2])
    ca = st.sidebar.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
    thal = st.sidebar.selectbox("Thalassemia", [0, 1, 2, 3])

    return {
        'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,
        'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach,
        'exang': exang, 'oldpeak': oldpeak, 'slope': slope,
        'ca': ca, 'thal': thal
    }

input_data = user_input()

if st.button("Predict"):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    st.subheader("Result")
    st.write("Prediction:", "Heart Disease" if prediction == 1 else "No Heart Disease")
    st.write("Probability of Heart Disease: {:.2%}".format(probability))