import os


def use_seek():
    """
    seek(offset, whence)
    :return:
    """
    file = open('file', mode='r', encoding='utf-8')
    file.seek(5, os.SEEK_SET)  # 相较于文件开头偏移5个字节
    text = file.read(5)
    print(text)
    file.close()


def use_seek_b_cur():
    """
    b模式下，读取到的是字节流，用于读取视频、音频、图片
    :return:
    """
    file = open('file', mode='rb+')
    file.seek(4, os.SEEK_CUR)
    file.seek(-2, os.SEEK_CUR)
    b = file.read()  # b模式下读取到的是字节流
    print(b)
    file.close()


def scan_dir(cur_path, width):
    """
    目录的深度优先遍历
    :param cur_path:
    :return:
    """
    file_list = os.listdir(cur_path)
    for file in file_list:
        print(" " * width, file)
        new_path = cur_path + '/' + file
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


if __name__ == '__main__':
    scan_dir('.', 0)
