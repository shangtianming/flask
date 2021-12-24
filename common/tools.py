from common import logging


def case_assert(*arg):
    print()
    result = True
    if arg:
        for i in arg:
            if eval(f"i[1] {i[0]} i[2]"):
                print(f"断言成功==>  {i[1]} {i[0]} {i[2]}")
            else:
                result = False
                print(f"断言失败==>  {i[1]} {i[0]} {i[2]}")
    assert result


def link_condition(**data):
    '''value目前只考虑了str、tuple、数字类型'''
    s = ''
    if data:
        for key, value in data.items():
            if isinstance(value, str):
                s += f" and {key} = '{value}' " if value else ''
            elif isinstance(value, tuple):
                if len(value) > 1:
                    s += f" and {key} in {value} " if value else ''
                elif len(value) == 1 and isinstance(value[0], str):
                    s += f" and {key} = '{value[0]}' " if value else ''
                else:
                    s += f" and {key} = {value[0]} " if value else ''
            else:
                s += f" and {key} = {value} " if value else ''
    return " where 1=1 " + s


if __name__ == '__main__':
    s = link_condition(a=1, b="1", c=(1, "2"))
    print(s)
