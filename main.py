from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

inventory = []

@app.post("/items/")
async def create_item(item: Item):
    inventory.append(item)
    return item

@app.get("/items/", response_model=List[Item])
async def read_items():
    return inventory
