# 这个Config配置类其实是修改BaseModel的默认行为的，也可以用来扩充功能
# 更多配置选项：https://pydantic-docs.helpmanual.io/usage/model_config/#options
from pydantic import BaseModel, ValidationError
from typing import Union


# CASE1: 使用配置类限制最大字符长度
class Mymodel(BaseModel):
    v: str

    class Config:
        max_anystr_length = 10 # 字符串最大长度为10字符
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length: {limit_value}',
        }


# CASE2: 使用配置类增加属性名称可以使用驼峰命名 alias
def to_camel(string: str) -> str:
    return ''.join(word.capitalize() for word in string.split('_'))


class Voice(BaseModel):
    name: str
    language_code: str

    class Cofnig:
        alias_generator = to_camel


# CASE3: smart_union 多种类型种匹配最合适的
class Model(BaseModel):
    x: Union[str, int]


class ModelSmart(BaseModel): # 可以直接在定义时指定配置 class ModelSmart(BaseModel, smart_union=True)
    x: Union[str, int]

    class Config:
        smart_union = True


if __name__ == '__main__':
    # CASE1: 
    try:
        Mymodel(v="*" * 20)
    except ValidationError as e:
        print(e)

    # CASE2: 
    voice = Voice(name='Filiz', language_code='zh-CN') # 这里已经使用驼峰命名了
    print(voice.language_code) # 使用原来的名称输出
    print(voice.dict(by_alias=True)) # key使用驼峰命名输出全部字典内容

    # CASE3:
    print(Model(x=1)) # 1被第一个str匹配，指定为字符串类型
    print(ModelSmart(x=1)) # 1被int匹配，指定为数字，数字更接近原代码意图
