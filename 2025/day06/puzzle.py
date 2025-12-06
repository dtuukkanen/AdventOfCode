# Hyvää itsenäisyyspäivää! 🇫🇮🎉

def read_input():
    with open("input.txt") as f:
        lines = f.readlines()

    all_digits = []
    operators = []

    for line in lines:
        line = line.strip()

        # Choose only lines that start with a digit
        if line[0].isdigit():
            digits = list(map(int, line.split()))
            all_digits.append(digits)
        else:
            operators = line.split()

    return all_digits, operators

def puzzle1():
    all_digits, operators = read_input()

    total = []
    for i in range(len(operators)):
        operator = operators[i]
        calc = all_digits[0][i]
        for j in range(1, len(all_digits)):
            if operator == "+":
                calc += all_digits[j][i]
            elif operator == "*":
                calc *= all_digits[j][i]
        total.append(calc)

    grand_total = sum(total)
    print("Puzzle 1:", grand_total)

if __name__ == "__main__":
    puzzle1()
