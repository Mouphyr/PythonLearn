import re

def demo1():
    ret=re.match(r'[hH]ello', 'Hello Python')
    if ret:
        print(ret.group())
    ret=re.match(r'[hH]ello', 'hello Python')
    if ret:
        print(ret.group())

    # 匹配多个字符
    ret=re.match(r'[a-z]+', 'hello Python')
    if ret:
        print(ret.group())

def demo2():
    """
    了解$的用法
    匹配0-99之间的数字
    :return:
    """
    ret=re.match(r'[1,9]?\d$','09')
    if ret:
        print(ret.group())
    else:
        print("无效")

def demo3():
    """
    匹配1-99之间的数字
    技巧: 十位数和个位数分开匹配 -> 利用「分组」
    匹配分组，依次匹配，写到前面的先匹配
    :return:
    """
    ret=re.match(r'[1-9][0-9]|[1-9]','11')
    if ret:
        print(ret.group())
    else:
        print("无效")

def demo4():
    email_list=['1234drgv@qq.com', '1256@163.com',
                '123sdrg6@gmail.com','2jdhfks@163.com']
    for email in email_list:
        ret=re.match(r'\w{4,20}@(163|gmail)\.com', email)
        if ret:
            print(f"正确的邮箱：{ret.group()}")
        else:
            print(f"无效的邮箱：{email}")

def demo_group():
    """
    依次打印分组
    ^代表匹配开头，[^-]*表示没有遇到‘-’就一直进行匹配（[]与^组合使用）
    :return:
    """
    ret=re.match(r'([^-]*)(-)(\d+)','a10-123456')
    print(ret.group(0))  # 等价于group()
    print(ret.group(1))
    print(ret.group(2))
    print(ret.group(3))

if __name__ == '__main__':
    demo_group()