floor = 0

with open("input.txt") as f:
    data = f.read().strip()
    for char in data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

print(floor)
