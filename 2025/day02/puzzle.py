def check_range(start, end, number):
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

def puzzle1():
    # Read input file
    id_sum = 0
    with open('input.txt') as f:
        line = f.readline()
    ids = line.split(',')

    # Go through each id range and sum valid ids
    for id in ids:
        start, end = map(int, id.split('-'))
        id_sum += check_range(start, end, id)

    print("ID Sum for Puzzle 1:", id_sum)

if __name__ == '__main__':
    puzzle1()
