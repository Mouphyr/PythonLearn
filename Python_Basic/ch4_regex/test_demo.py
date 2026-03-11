import re

# 读取文件内容
f=open("test_file", mode="r", encoding="utf-8")
content = f.read()  # 读取整个文件内容为字符串

# 示例1：匹配所有有效的11位手机号（开头为13/18）
phone_pattern = r"1[38]\d{9}"  # 正则规则：1开头，第二位3/8，后面9位数字
phones = re.findall(phone_pattern, content)
print("匹配到的有效手机号：", phones)

# 示例2：匹配所有年-月-日格式的日期
date_pattern = r"\d{4}-\d{2}-\d{2}"  # 正则规则：4位年-2位月-2位日
dates = re.findall(date_pattern, content)
print("匹配到的年-月-日：", dates)

# 示例3：匹配所有简单邮箱
email_pattern = r"\w+@\w+\.\w+"  # 正则规则：字母/数字/下划线@字母/数字.字母
emails = re.findall(email_pattern, content)
print("匹配到的邮箱：", emails)
