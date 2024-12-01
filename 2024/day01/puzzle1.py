left_values = []
right_values = []

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        left, right = line.split("   ")
        left_values.append(int(left))
        right_values.append(int(right))

distances = 0
left_values.sort()
right_values.sort()
for i in range(len(left_values)):
    distances += abs(left_values[i] - right_values[i])

print(distances)
