left_values = []
right_values = []

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split("   ")
        left_values.append(int(left))
        right_values.append(int(right))

similarities = 0
left_values.sort()
right_values.sort()
for value in left_values:
    similarities += value * right_values.count(value)

print(similarities)
