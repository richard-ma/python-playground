# dataclass 如果不想使用继承BaseModel的方法来获得pydantic支持，可以使用dataclass装饰器来装饰类

from pydantic.dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime = None


user = User(id='42', signup_ts='2032-02-22T12:00')
print(user)
