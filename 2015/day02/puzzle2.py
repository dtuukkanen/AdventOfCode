with open("input.txt") as f:
    total = 0
    for line in f:
        l, w, h = sorted(map(int, line.split("x")))
        ribbon = 2 * l + 2 * w + l * w * h
        total += ribbon

print(total)
