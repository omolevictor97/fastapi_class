import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
X_train, X_test, y_train, y_test =train_test_split(df.drop("variety", axis=1), df.variety, random_state=42)

with st.sidebar:
    st.markdown("---")
    st.markdown("__*IRIS CLASSIFICATION*__")
    st.markdown("---")
    st.image(image="iris.png", caption="Iris Flower")

with open("preprocessor.pkl", "rb") as processor:
    preprocessor = pickle.load(processor)

with open("classifier.pkl", "rb") as model:
    model = pickle.load(model)

with open("labels.pkl", "rb") as labels:
    le= pickle.load(labels)

y_train = le.fit_transform(y_train)

X_train = preprocessor.fit_transform(X_train, y_train)

st.markdown("""
    <style>
            eyeqlp51.st-emotion-cache-1pbsqtx.ex0cdmw0 {
            visible: hidden;
            }
    </style>
""", unsafe_allow_html=True)

st.title(body="Iris Flower Classification")
sep_length = st.number_input(label="Enter Sepal Length", min_value=0.0, max_value=10.0)
sep_width  = st.number_input(label="Enter Sepal Width", min_value=0.0, max_value=7.8)
pet_width  = st.number_input(label="Enter Petal Width", min_value=0.0, max_value=7.8)
pet_length  = st.number_input(label="Enter Petal Length", min_value=0.0, max_value=7.8)

def predict(sep_length, sep_width, pet_width, pet_length):

    input_data = {
            "sepal.length": sep_length,
            "sepal.width" : sep_width,
            "petal.length" : pet_length,
            "petal.width" : pet_width
        }
    df = pd.DataFrame([input_data])
    processed_data = preprocessor.transform(df)
    #st.write(processed_data)
    pred = model.predict(processed_data)[0]
    st.success(f'Your Prediction is {le.inverse_transform([pred])[0]}' , icon="✅")



if st.button("Predict"):
    predict(sep_length, sep_width, pet_length, pet_width)
    st.snow()
