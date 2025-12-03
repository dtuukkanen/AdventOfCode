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

def puzzle2():
    result = 0

    # Read input file
    lines = read_file()

    # Process each line
    for line in lines:
        n = len(line)
        k = 12  # number of batteries to keep

        # Use a greedy algorithm to find the lexicographically largest subsequence
        result_indices = []
        start = 0

        for i in range(k):
            # We need to pick k-i more digits from position start onwards
            # We must leave at least k-i-1 digits after our choice
            max_digit = '0'
            max_pos = start

            # Find the largest digit in the valid range
            for j in range(start, n - (k - i - 1)):
                if line[j] > max_digit:
                    max_digit = line[j]
                    max_pos = j

            result_indices.append(max_pos)
            start = max_pos + 1

        # Build the result string
        joltage_str = ''.join([line[i] for i in result_indices])
        joltage = int(joltage_str)

        result += joltage

    print("Puzzle 2 battery sum:", result)

if __name__ == '__main__':
    puzzle1()
    puzzle2()
