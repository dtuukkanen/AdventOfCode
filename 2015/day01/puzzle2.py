with open("input.txt") as f:
    data = f.read().strip()
    floor = 0
    for i, char in enumerate(data):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            print(i + 1)
            break
