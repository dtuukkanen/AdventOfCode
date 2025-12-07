import math

def puzzle1():
    with open('input.txt') as f:
        lines = f.readlines()

    width = len(lines[0].strip())
    split = 0

    # Update second row
    start = lines[0].index("S")
    lines[1] = lines[1][:start] + "|" + lines[1][start + 1:]

    for i in range(2, len(lines)):
        for j in range(width):
            prev_char = lines[i - 1][j]
            cur_char = lines[i][j]

            if prev_char == "|" and cur_char == ".":
                lines[i] = lines[i][:j] + "|" + lines[i][j + 1:]
            elif prev_char == "|" and cur_char == "^":
                lines[i] = lines[i][:j-1] + "|" + cur_char + "|" + lines[i][j + 2:]
                split += 1

    print("Puzzle 1:", split)

def puzzle2():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    width = len(lines[0])
    options = 0

    # Convert the grid to a list of lists, parsing initial non-numeric characters.
    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)

    # Find 'S' and replace the position below it with the number 1.
    start_j = lines[0].find('S')
    if start_j != -1:
        grid[1][start_j] = 1

    # Process the grid row by row, starting from the second row.
    for i in range(1, len(grid) - 1):
        current_row = grid[i]
        next_row = grid[i + 1][:]  # Make a copy of the next row's structure

        for j in range(width):
            # Rule 1: A number falls down.
            if isinstance(current_row[j], int):
                # If it lands on a '.', it continues down.
                if next_row[j] == '.':
                    next_row[j] = current_row[j]
                # If it lands on another number, they merge.
                elif isinstance(next_row[j], int):
                    next_row[j] += current_row[j]
                # If it lands on a splitter '^'.
                elif next_row[j] == '^':
                    # It splits left and right.
                    # Left path
                    if j > 0:
                        if isinstance(next_row[j - 1], int):
                            next_row[j - 1] += current_row[j]
                        else:
                            next_row[j - 1] = current_row[j]
                    # Right path
                    if j < width - 1:
                        if isinstance(next_row[j + 1], int):
                            next_row[j + 1] += current_row[j]
                        else:
                            next_row[j + 1] = current_row[j]

        # Update the grid with the newly computed row.
        grid[i + 1] = next_row

    # Calculate the sum of all numbers in the last row.
    final_row = grid[-1]
    for cell in final_row:
        if isinstance(cell, int):
            options += cell

    print("Puzzle 2:", options)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
