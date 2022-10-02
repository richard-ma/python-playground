from fastapi import FastAPI, Query
from typing import Union


app = FastAPI()


# 查询参数q，默认值是None，最短3字符，最长50字符
# 添加正则表达式
# alias, title, description, deprecated
@app.get('/items/')
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_lenght=50, regex="^test$")):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results
