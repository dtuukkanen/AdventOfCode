def create_matrix():
    with open("input.txt") as f:
        data = f.readlines()
        matrix = []
        for line in data:
            line = line.strip()
            matrix.append(list(line))
    return matrix

def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "^":
                return i, j
    return -1, -1

def print_matrix(matrix):
    for line in matrix:
        print(line)

def count_paths(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "^" or matrix[i][j] == "v" or matrix[i][j] == ">" or matrix[i][j] == "<":
                count += 1
    return count


def main():
    matrix = create_matrix()
    i, j = find_start(matrix)
    print("START:", i, j)
    direction = "^"
    while True:
        # Check direction
        next_i, next_j = i, j
        if direction == "^":
            next_i -= 1
        elif direction == "v":
            next_i += 1
        elif direction == ">":
            next_j += 1
        elif direction == "<":
            next_j -= 1

        if next_i < 0 or next_i >= len(matrix) or next_j < 0 or next_j >= len(matrix[next_i]):
            break

        # Check obstacle
        if matrix[next_i][next_j] == "#":
            # Change direction to the right (clockwise rotation)
            if direction == "^":
                direction = ">"
            elif direction == ">":
                direction = "v"
            elif direction == "v":
                direction = "<"
            elif direction == "<":
                direction = "^"
        else:
            i, j = next_i, next_j
        matrix[i][j] = direction

    print_matrix(matrix)
    print("total distinct paths:", count_paths(matrix))

main()
