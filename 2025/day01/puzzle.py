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

    print("Password:", password)

if __name__ == "__main__":
    puzzle1()
