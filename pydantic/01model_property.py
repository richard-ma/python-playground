from pydantic import BaseModel


class Mymodel(BaseModel):
    id: int
    name = 'my name'

if __name__ == '__main__':
    external_data = {
        'id': 33
    }

    my_model = Mymodel(**external_data)

    ################################### Model Property ########################
    # 查看id初始化是否成功
    assert my_model.id == 33

    # 为id赋值
    my_model.id = 44
    assert my_model.id == 44

    # 初始化时，field只有id一个字段
    assert my_model.__fields_set__ == {'id'}

    # 将对象转换为字典
    assert my_model.dict() == dict(my_model) == {'id': my_model.id, 'name': my_model.name}

    # 将对象转换为JSON
    print('************** .json() *************')
    print(my_model.json())

    # TODO: 复制对象,检查对象地址是否一致
    another_my_model = my_model.copy()
    assert my_model == another_my_model

    # 从字典到对象
    obj_from_dict = Mymodel.parse_obj({
        'id': 88,
        'name': 'hello',
    })
    assert obj_from_dict.id == 88

    # 从字符串到对象
    data_string = '{"id": 43, "name": "bye"}'
    obj_from_string = Mymodel.parse_raw(data_string)

    assert obj_from_string.dict() == {'id': 43, 'name': 'bye'}

    # 将对象转换为schema
    print('************** .schema() *************')
    print(my_model.schema())

    # 将对象转换为schema json
    print('************** .schema_json() *************')
    print(my_model.schema_json())

    # __fields_set__
    print('************** .__fields_set__ *************')
    print(my_model.__fields_set__)

    # __fields__
    print('************** .__fields__ *************')
    print(my_model.__fields__)

    # __config__ config class
    print('************** .__config__ *************')
    print(my_model.__config__)
