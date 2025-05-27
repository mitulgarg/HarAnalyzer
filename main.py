from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database (for demonstration purposes)
items = []

# Pydantic model for item data
class Item(BaseModel):
    name: str
    description: str

# Create an item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item.name=item.name+" after running API"
    items.append(item)
    return item