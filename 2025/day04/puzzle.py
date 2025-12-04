def puzzle1():
    result = 0

    with open('input.txt') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        row_length = len(lines[i])
        for j in range(len(lines[i])):
            adjacent_papers = 0

            if lines[i][j] == "@":
                for step_x in range(-1, 2):
                    for step_y in range(-1, 2):
                        # Skip the current position
                        if step_x == 0 and step_y == 0:
                            continue

                        # Calculate new positions to check
                        new_x = i + step_x
                        new_y = j + step_y
                        # Check bounds
                        if 0 <= new_x < len(lines) and 0 <= new_y < row_length:
                            if lines[new_x][new_y] == "@":
                                adjacent_papers += 1

                if adjacent_papers < 4:
                    result += 1
    print(result)

if __name__ == '__main__':
    puzzle1()