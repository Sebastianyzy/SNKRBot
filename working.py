from typing import ItemsView
import fastapi
from fastapi import FastAPI, Path
from starlette.routing import PARAM_REGEX

app = FastAPI()
inventory = {1:{"name": "Milk", "price": 3.99, "brand":"regular"}}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item",gt=0,lt=4) ):
    return inventory[item_id]     