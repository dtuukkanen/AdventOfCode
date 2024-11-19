def init_matrix():
    matrix = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def count_neighbors_on(matrix, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: # Skip the current cell
                continue
            if x + i < 0 or x + i >= len(matrix): # Skip out of bounds
                continue
            if y + j < 0 or y + j >= len(matrix[0]): # Skip out of bounds
                continue
            if matrix[x + i][y + j] == '#':
                count += 1
    return count

def next_state(matrix):
    new_matrix = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count = count_neighbors_on(matrix, i, j)
            if (i == 0 or i == len(matrix) - 1) and (j == 0 or j == len(matrix[0]) - 1):
                new_matrix[i][j] = '#'
            elif matrix[i][j] == '#':
                if count == 2 or count == 3:
                    new_matrix[i][j] = '#'
            else:
                if count == 3:
                    new_matrix[i][j] = '#'
    return new_matrix

def count_lights(matrix):
    count = 0
    for row in matrix:
        count += row.count('#')
    return count

def main():
    matrix = init_matrix()
    for _ in range(100):
        matrix = next_state(matrix)
    print(count_lights(matrix))

main()
