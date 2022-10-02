from typing import Union
from fastapi import FastAPI, Path, Query
from typing import Union


app = FastAPI()


@app.get('/items/{item_id}')
async def read_items(
    item_id: int = Path(title='The ID of the item to get', ge=0, le=1000), # 0 <= item_id <= 1000
    q: Union[str, None] = Query(default=None, alias='item-query'), # ?item-query=xxx
    size: float = Query(gt=0, lt=10.5) # 0 < size < 10.5
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
