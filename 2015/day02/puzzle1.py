with open("input.txt") as f:
    total = 0
    for line in f:
        l, w, h = map(int, line.split("x"))
        area = 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
        total += area

print(total)
