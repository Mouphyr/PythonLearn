def open_r():
    """
    读取文件
    :return:
    """
    file = open('file', mode='r', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()


def open_a():
    """
    追加文本
    :return:
    """
    file = open('file', mode='a', encoding='utf-8')
    file.write('\n你好')


def use_readline():
    file = open('file')
    while True:
        text = file.readline()
        if not text:
            break
        print(text, end='')


if __name__ == '__main__':
    # open_a()
    use_readline()
