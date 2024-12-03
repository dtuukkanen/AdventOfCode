import re

multiplications = 0
with open("input.txt", "r") as f:
    data = f.read()
    tasks = re.findall(r"mul\(\d+,\d+\)", data)
    for task in tasks:
        a, b = map(int, re.findall(r"\d+", task))
        multiplications += a * b
print(multiplications)
