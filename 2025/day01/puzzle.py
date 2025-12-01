def puzzle1():
    cursor = 50

    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Password is the times of cursor pointing to zero
    password = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())
        if direction == "L":
            cursor -= value
        elif direction == "R":
            cursor += value

        cursor %= 100

        if cursor == 0:
            password += 1

    print("Password for Puzzle 1:", password)

def puzzle2():
    cursor = 50

    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Password is the times of cursor pointing to zero
    password = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:].strip())
        delta = -value if direction == "L" else value

        start_abs = cursor
        end_abs = cursor + delta

        # Number of times multiples of 100 are crossed between start_abs and end_abs
        if end_abs > start_abs:
            rotations = end_abs // 100 - start_abs // 100
        elif end_abs < start_abs:
            rotations = (start_abs - 1) // 100 - (end_abs - 1) // 100
        else:
            rotations = 0

        password += abs(rotations)
        cursor = end_abs % 100

    print("Password for Puzzle 2:", password)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
