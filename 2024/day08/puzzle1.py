def read_input():
    matrix = []
    with open('input.txt') as f:
        for line in f:
            matrix.append(list(line.strip()))
    return matrix

    
def find_antennas(data):
    antennas = {}
    for i, line in enumerate(data):
        for j, mark in enumerate(line):
            if mark == ".":
                continue
            else:
                if mark not in antennas:
                    antennas[mark] = [(i, j)]
                else:
                    antennas[mark].append((i, j))
    return antennas


def mark_antinodes(data, antennas):
    for antenna in antennas:
        for index1 in range(0, len(antennas[antenna]) - 1):
            for index2 in range(index1 + 1, len(antennas[antenna])):
                node1 = antennas[antenna][index1]
                node2 = antennas[antenna][index2]
                i1, j1 = node1
                i2, j2 = node2

                diff_i = i2 - i1
                diff_j = j2 - j1

                # Mark antinode for first antenna
                mark_antinode(data, i2 + diff_i, j2 + diff_j)

                # Mark antinode for second antenna
                mark_antinode(data, i1 - diff_i, j1 - diff_j)


def mark_antinode(data, i, j):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return
    data[i][j] = "#"


def print_matrix(data):
    for line in data:
        print("".join(line))

def count_uniques(data):
    count = 0
    for line in data:
        for mark in line:
            if mark == "#":
                count += 1
    return count


def main():
    data = read_input()
    print_matrix(data)
    antennas = find_antennas(data)
    print_matrix(data)
    mark_antinodes(data, antennas)
    print("Antennas: ", antennas)
    print_matrix(data)
    print("Unique nodes: ", count_uniques(data))

main()

