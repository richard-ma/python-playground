from fastapi import FastAPI
from typing import Union


app = FastAPI()

fake_items_db = [{'item_name': 'foo'}, {'item_name': 'bar'}, {'item_name': 'baz'}]


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10): # default value
    return fake_items_db[skip: skip + limit]

# q为可选参数，默认值是None
@app.get('/items/{item_id}')
async def read_item_by_id(item_id: str, q: Union[str, None] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

# 查询参数类型
# 1. 必须参数 必须写，且必须给出值
# 2. 有默认值的参数，例如s int = 0 可以不写，不写为默认值
# 3. 可选的参数，例如q Union[str, None] = None 可以不写，不写则为None
