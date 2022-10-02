# 自定义导出model的属性
from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

print(m.dict())

print(m.dict(include={'foo', 'bar'})) # 仅输出include列出的属性
print(m.dict(exclude={'foo', 'bar'})) # 不输出exclude列出的属性


# BaseModel.copy()
print(m.copy(include={'foo', 'bar'})) # 仅拷贝include列出的属性
print(m.copy(exclude={'foo', 'bar'})) # 不拷贝exclude列出的属性
print(m.copy(update={'banana': 0})) # 更新部分属性后拷贝
print(id(m.bar), id(m.copy().bar)) # 两个bar地址相同，copy默认是浅拷贝
print(id(m.bar), id(m.copy(deep=True).bar)) # 两个bar地址不同，加了deep参数的是深拷贝


# 自定义include和exclude，可以精确到字段
