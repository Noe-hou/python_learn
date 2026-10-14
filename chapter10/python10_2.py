#练习1
from pathlib import Path

name=input("请输入名字：")
path=Path('guest.txt')

path.write_text(name)
print("名字已保存至guest.txt")

#练习2
contents=''
active=True
while active:
    names=input("名字：").strip().lower()
    if names=="q":
        active=False
        break
    else:
        contents+=names+"\n"
   
paths=Path('guest_book.txt')
paths.write_text(contents)
print("已经存入guest_book.txt")
