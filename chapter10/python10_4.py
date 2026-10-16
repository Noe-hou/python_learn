import json
from pathlib import Path
#练习1
num=int(input("输入你喜欢的数："))
path=Path('num.json')
contents=json.dumps(num)
path.write_text(contents,encoding="utf-8")
print("已保存")
nums=json.loads(contents)
print(nums)

#练习2
path=Path('user_imfo.text')
try:
    text=path.read_text()
    user_info=json.loads(text)
    print("程序记住了你的信息：")
    print(f"用户名：{user_info['username']}")
    print(f"爱好：{user_info['hobby']}")
    print(f"家乡：{user_info['hometown']}")
except FileNotFoundError:
    username=input("输入用户名：")
    hobby=input("输入爱好：")
    hometown=input("输入家乡：")
    user_info={"username":username,
               "hobby":hobby,
               "hometown":hometown}
    path.write_text(json.dumps(user_info),encoding='utf-8')
    print("你的信息已保存")
