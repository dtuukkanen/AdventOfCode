import re

multiplications = 0
do = True
with open("input.txt", "r") as f:
    data = f.read()
    tasks = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    for task in tasks:
        if task == "do()":
            do = True
        elif task == "don't()":
            do = False
        else:
            if do:
                a, b = map(int, re.findall(r"\d+", task))
                multiplications += a * b
print(multiplications)
