from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel



app = FastAPI()

# In-memory database (for demonstration purposes)
items = []

class Item(BaseModel):
    name: str

@app.get("/items/", response_model=Item)
async def get_item(name: str = Query(..., description="Name to process")):
    reversed_name = name[::-1]
    item = Item(name=reversed_name)
    items.append(item)
    return item