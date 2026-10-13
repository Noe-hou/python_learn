#练习1
from pathlib import Path
path=Path('learning_python.txt')
print(path.read_text())

#练习2
contents=path.read_text()
lines=contents.splitlines()
for line in lines:
    new_lines=line.replace("Python","C")
    print(new_lines)
