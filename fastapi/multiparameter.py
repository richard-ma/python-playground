from fastapi import FastAPI  # type: ignore
from typing import Union
from pydantic import BaseModel  # type: ignore


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


# 同时使用Item和User两个参数
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, user: User):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results