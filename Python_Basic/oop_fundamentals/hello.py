def mul_chart():
    """
    打印九九乘法表
    :return:
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            if j == i:
                print(j, "*", i, "=", i * j)
            else:
                print(j, "*", i, "=", i * j, end="\t")


def use_find():
    my_str = input("请输入字符串：")
    print(my_str.find('cd', 4))


def str_slice():
    num_str = "0123456789"
    print(num_str[2:6])  # 2345
    print(num_str[::2])  # 02468


def my_sum(*args):
    the_sum = 0
    for i in args:
        the_sum += i
    return the_sum


def step(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        return step(n - 1) + step(n - 2) + step(n - 3)


if __name__ == '__main__':
    print(step(10))
