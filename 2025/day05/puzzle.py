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

def puzzle2():
    ranges, _ = read_input()

    # Sort ranges by their start value
    ranges.sort(key=lambda x: x[0])

    # Start merging ranges with the smallest start value
    merged_ranges = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if current_start <= last_end + 1:
            # Merge overlapping or contiguous ranges
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add new range
            merged_ranges.append((current_start, current_end))

    total_valid_count = sum(end - start + 1 for start, end in merged_ranges)
    print(f"Puzzle 2: {total_valid_count}")

if __name__ == "__main__":
    puzzle1()
    puzzle2()
