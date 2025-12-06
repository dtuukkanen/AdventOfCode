# Hyvää itsenäisyyspäivää! 🇫🇮🎉
import math

def read_input():
    with open("2025/day06/input.txt") as f:
        lines = f.readlines()

    all_digits = []
    operators = []

    for line in lines:
        line = line.strip()

        # Choose only lines that start with a digit
        if line[0].isdigit():
            digits = line.split()
            all_digits.append(digits)
        else:
            operators = line.split()

    return all_digits, operators

def puzzle1():
    all_digits, operators = read_input()

    total = []
    for i in range(len(operators)):
        operator = operators[i]
        calc = int(all_digits[0][i])
        for j in range(1, len(all_digits)):
            if operator == "+":
                calc += int(all_digits[j][i])
            elif operator == "*":
                calc *= int(all_digits[j][i])
        total.append(calc)

    grand_total = sum(total)
    print("Puzzle 1:", grand_total)

## PUZZLE 2 ##


def read():
    with open("2025/day06/input.txt") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in raw_lines)
    padded = [line.ljust(width) for line in raw_lines]

    digit_rows = padded[:-1]
    operator_row = padded[-1]

    def is_separator(col: int) -> bool:
        return all(row[col] == " " for row in padded)

    problems = []
    col = width - 1
    while col >= 0:
        if is_separator(col):
            col -= 1
            continue

        numbers = []
        op = None
        while col >= 0 and not is_separator(col):
            if operator_row[col] in {"+", "*"}:
                op = operator_row[col]

            digits = [row[col] for row in digit_rows if row[col].isdigit()]
            if digits:
                numbers.append(int("".join(digits)))

            col -= 1

        if op is None:
            raise ValueError("No operator found for problem")

        problems.append((numbers, op))

    return problems


def puzzle2():
    problems = read()

    grand_total = 0
    for numbers, operator in problems:
        if operator == "+":
            subtotal = sum(numbers)
        else:
            subtotal = math.prod(numbers)
        grand_total += subtotal

    print("Puzzle 2:", grand_total)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()
