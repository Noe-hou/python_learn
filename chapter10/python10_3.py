#练习1
try:
    a=int(input("输入第一个数："))
    b=int(input("输入第二个数："))
    print(a+b)
except ValueError:
    print("请输入数字")

#练习2
while True:
    num1_str=input("输入第一个数字（输入q退出）：")
    if num1_str=="q":
        break
    num2_str=input("输入第二个数字（输入q退出）：")
    if num2_str=="q":
        break
    try:
        num1=int(num1_str)
        num2=int(num2_str)
        print(num1+num2)
    except ValueError:
        print("输入数字")

#练习3
from pathlib import Path
def read_file(path_name):
    try:
        path=Path(path_name)
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\n错误找不到{path_name}")
read_file('cats.txt')
read_file('dogs.txt')

#练习4
def count_word(filename1):
    try:
        path1=Path(filename1)
        contents=path1.read_text(encoding='utf-8').lower()
    except FileNotFoundError:
        print("文件找不到")
    else:
        count=contents.count("the")
        count_space=contents.count(" the ")
        print(f"统计‘the’{count}")
        print(f"统计‘ the ’{count_space}")
count_word("book.txt")
