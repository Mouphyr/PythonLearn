# sort()与sorted()的区别：sorted()不会改变原本的列表，而是会返回一个新建的列表

def change_lower(str_name:str):
    return str_name.lower()

def sort_str():
    my_list = "This is a test string".split()
    print(my_list)
    print(sorted(my_list))
    # key: 传递一个比较规则的函数
    print(sorted(my_list, key=change_lower))

def sort_with_lambda():
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'C', 10),
    ]
    print(sorted(student_tuples, key=lambda stu: stu[2]))

if __name__ == '__main__':
    sort_str()
    print('-'*50)
    sort_with_lambda()