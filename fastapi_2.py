from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.preprocessing import StandardScaler


app = FastAPI()

with open("classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length : float
    petal_width : float

@app.get("/")
def index():
    return "Prediction First Page"

@app.post("/predict")
def predict(iris:Iris):
    attributes = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
    scaled_attributes = StandardScaler().fit_transform(attributes)
    pred = model.predict(scaled_attributes)
    return f"Your predicted value is {pred[0]}"

