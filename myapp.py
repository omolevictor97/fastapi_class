from fastapi import FastAPI
import uvicorn
import fastapi
from pydantic import BaseModel

print(fastapi.__version__)



application = FastAPI() # Initiate the object of FastAPI class

@application.get("/") #Methods, there are other methods like Post, Put and delete, here we call '@' a path decorator
def myindex(): # path operation function
     c = "Hello Guys"
     return c

@application.get("/calculation/{num_1}")
async def myindex(num_1:float):
     return f"Our number is {num_1}"

class Item(BaseModel):
     quantity: int
     price: float
     ID : int

@application.post(path='/get_item')
def get_item(item : Item):
     normal_price = item.price * item.quantity
     if item.quantity >= 35:
          discounted_price = normal_price - (0.2 * normal_price)
          discount = normal_price - discounted_price
          return {"Discount" : discounted_price, "Normal Price": normal_price, "Discount": discount}          
     else:
          discounted_price = 0
          discount = normal_price - discounted_price
          return {"Discount" : discounted_price, "Normal Price": normal_price, "Discount": discount}

if __name__ == "__main__":
     uvicorn.run(app=application, host="127.0.0.1", reload=True, port=3000)

