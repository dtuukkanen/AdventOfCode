def read_input():
    with open('input.txt') as f:
        line = f.readline()
    ids = line.split(',')
    return ids

def check_range1(start, end, number):
    id_sum = 0

    for i in range(start, end + 1):
        # Convert to string to split
        str_i = str(i)

        # Find middle and check if halves are equal
        middle = len(str_i) // 2
        left, right = str_i[:middle], str_i[middle:]
        if left == right:
            id_sum += i

    return id_sum

def check_range2(start, end, number):
    id_sum = 0

    for i in range(start, end + 1):
        # Convert to string to split
        str_i = str(i)

        for j in range(1, len(str_i)):
            pattern = str_i[:j]
            repeated = pattern * (len(str_i) // len(pattern))
            if repeated == str_i:
                id_sum += i
                break

    return id_sum

def puzzle1():
    # Read input file
    id_sum = 0
    ids = read_input()

    # Go through each id range and sum valid ids
    for id in ids:
        start, end = map(int, id.split('-'))
        id_sum += check_range1(start, end, id)

    print("ID Sum for Puzzle 1:", id_sum)

def puzzle2():
    # Read input file
    id_sum = 0
    ids = read_input()

    # Go through each id range and sum valid ids
    for id in ids:
        start, end = map(int, id.split('-'))
        id_sum += check_range2(start, end, id)

    print("ID Sum for Puzzle 2:", id_sum)

if __name__ == '__main__':
    puzzle1()
    puzzle2()
