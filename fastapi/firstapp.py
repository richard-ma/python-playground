# 第一步
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello wolrd'}

# run app
# uvicorn fistapp:app --reload
