from pydantic import BaseModel, ValidationError


class Mymodel(BaseModel):
    v: str

    class Config:
        max_anystr_length = 10 # 字符串最大长度为10字符
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length: {limit_value}',
        }


if __name__ == '__main__':
    try:
        Mymodel(v="*" * 20)
    except ValidationError as e:
        print(e)
