def read_file():
    with open('input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def puzzle1():
    result = 0

    # Read input file
    lines = read_file()

    # Process each line
    for line in lines:
        # Initialize first and second largest numbers
        first_num = int(line[-2])
        second_num = int(line[-1])
        line_len = len(line)

        # Iterate through the line in reverse order
        for i in range(line_len-2, -1, -1):
            check_num = int(line[i])
            if check_num >= first_num:
                if first_num > second_num:
                    second_num = first_num
                first_num = check_num

        # Concat and change to string
        comb_str = int(str(first_num) + str(second_num))
        result += comb_str

    print("Puzzle 1 battery sum:", result)

if __name__ == '__main__':
    puzzle1()
