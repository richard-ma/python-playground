from pydantic import BaseModel, ValidationError, validator


class Mymodel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name') # 对name字段的验证器
    def name_must_contain_space(cls, v, values):
        if ' ' not in v:
            raise ValueError('must contain space')
        return v.title()

    # 对password2进行匹配验证，password2 == password1
    # 使用values来接收所有属性的值，是一个字典
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

if __name__ == '__main__':
    # 可以成功创建对象
    myobj = Mymodel(
        name='hello world',
        username='testname',
        password1='pw',
        password2='pw',
    )
    print(myobj)

    # 不能通过验证的对象
    try:
        myobj = Mymodel(
            name='helloworld', # 没有空格
            username='t,stname', # 含有标点
            password1='pwsss', # 两次密码不同
            password2='pw',
        )
    except ValidationError as e:
        print(e)
