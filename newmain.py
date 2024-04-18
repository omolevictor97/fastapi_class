import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split


#Reading dataset
df = pd.read_csv("iris.csv")
df = df.drop("Unnamed: 0", axis=1)

X_train, X_test, y_train, y_test = train_test_split(df.drop("variety", axis=1), df.variety, random_state=42)

with st.sidebar:
    st.markdown("""
---
  <center> <h1> Yemi's Farm </h1></center>
                         
---
""", unsafe_allow_html=True)
    
    st.image(image='iris.png', caption="Iris Flower")


# Unpickle or deserialize your pickled model

with open("classifier.pkl", "rb") as model:
    model = pickle.load(model)

with open("preprocessor.pkl", "rb") as preprocessor:
    processor = pickle.load(preprocessor)

with open("labels.pkl", "rb") as labels:
    le = pickle.load(labels)

X_train = processor.fit_transform(X_train, y_train)
st.title(body="Iris Classification")

a = st.number_input(label="Enter sepal Length", min_value=0.0, max_value=10.0)
b = st.number_input(label="Enter Sepal Width", min_value=0.0, max_value=10.0)
c = st.number_input(label="Enter Petal Length", min_value=0.0, max_value=10.0)
d = st.number_input(label="Enter Petal Width", min_value=0.0, max_value=10.0)

def predict(sep_length, sep_width, pet_length, pet_width):
    input_data = {
        "sepal.length": sep_length,
        "sepal.width" : sep_width,
        "petal.length" : pet_length,
        "petal.width" : pet_width
    }

    data = pd.DataFrame([input_data])
    st.write(data)
    processed_data = processor.transform(data)
    st.write(processed_data)

    preds = model.predict(processed_data)[0]
    st.success(f'Your Prediction is {le.inverse_transform([preds])[0]}' , icon="✅")

if st.button("Predict"):
    predict(sep_length=a, sep_width=b, pet_length=c, pet_width=d)
    st.snow()
