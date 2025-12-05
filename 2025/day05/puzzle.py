def read_input():
    ranges = []
    ingredients = []

    with open("input.txt") as f:
        lines = f.readlines()
        split_index = lines.index("\n")

        # Read ranges
        for line in lines[:split_index]:
            line = line.strip()
            start, end = line.split("-")
            ranges.append((int(start), int(end)))

        # Read ingredients
        for line in lines[split_index + 1:]:
            line = line.strip()
            ingredients.append(int(line))

    return ranges, ingredients

def puzzle1():
    ranges, ingredients = read_input()
    valid_count = 0

    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                valid_count += 1
                break

    print(f"Puzzle 1: {valid_count}")

if __name__ == "__main__":
    puzzle1()
