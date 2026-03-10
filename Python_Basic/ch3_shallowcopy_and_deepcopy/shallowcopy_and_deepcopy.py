import copy

def use_shallow_copy():
    """
    copy()是浅拷贝
    :return:
    """
    a=[1,2]
    b=[3,4]
    plus1=[a,b]
    plus2=copy.copy(plus1)
    a[0]=10
    # 可变数据类型内包含可变数据类型
    # 此时浅拷贝会导致 plus1 和 plus2 两个数组都发生改变
    print(f'plus1 {plus1}')
    print(f'plus2 {plus2}')

def use_deep_copy():
    """
    deepcopy()是深拷贝
    :return:
    """
    a=[1,2]
    b=[3,4]
    plus1=[a,b]
    plus2=copy.deepcopy(plus1)
    a[0]=10
    # 此时深拷贝只会改变 plus1
    print(f'plus1 {plus1}')
    print(f'plus2 {plus2}')

class Student:
    """
    name和age都是不可变类型，使用浅拷贝即可
    """
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

class Teacher:
    """
    由于teach_class是可变数据类型，所以需要深拷贝
    """
    def __init__(self,name:str,teach_class:list):
        self.name=name
        self.teach_class=teach_class

if __name__ == '__main__':
    use_shallow_copy()
    print('-'*50)
    use_deep_copy()