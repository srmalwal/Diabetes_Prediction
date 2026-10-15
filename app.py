import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diabetes_model.pkl", "rb"))
# scaler = pickle.load(open("diabetes_features.pkl", "rb"))

st.title("Diabetes Prediction System")

pregnancies = st.number_input("Pregnancies", value=0)

glucose = st.number_input("Glucose", value=100)

blood_pressure = st.number_input("Blood Pressure", value=80)

skin_thickness = st.number_input("Skin Thickness", value=20)

insulin = st.number_input("Insulin", value=100)

bmi = st.number_input("BMI", value=18)

diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", value=0.3)

age = st.number_input("Age", value=30)

if st.button("Predict"):

    data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree_function,
        age
    ]])

    # data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Model prediction: Diabetes-positive")
    else:
        st.success("Model prediction: Diabetes-negative")