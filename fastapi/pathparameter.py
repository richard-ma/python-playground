from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# http://localhost:8000/items
# 优先匹配/items，如果有参数则匹配/items/{item_id}
@app.get('/items')
async def read_items():
    return {'item_id': 'default'}

# http://localhost:8000/items/33
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

# type Enum
# http://localhost:8000/models/{model_name}
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    return {'model_name': model_name}

