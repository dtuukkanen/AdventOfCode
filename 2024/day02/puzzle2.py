def is_valid_differences(levels):
    # Check if differences between adjacent levels are between 1 and 3
    for i in range(len(levels)-1):
        diff = abs(levels[i] - levels[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def increasing_or_decreasing(levels):
    if (all(levels[i] <= levels[i+1] for i in range(len(levels)-1)) or
        all(levels[i] >= levels[i+1] for i in range(len(levels)-1))):
        return True

def is_safe_with_dampener(levels):
    # If already valid and decreasing, it's safe
    if is_valid_differences(levels) and increasing_or_decreasing(levels):
        return True

    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new list without the level at position i
        reduced_levels = levels[:i] + levels[i+1:]
        # Check if this makes it valid and decreasing
        if (is_valid_differences(reduced_levels) and
            increasing_or_decreasing(reduced_levels)):
            return True

    return False

# Read the input
with open('input.txt') as f:
    lines = f.readlines()

safe_count = 0
for line in lines:
    levels = list(map(int, line.strip().split()))
    if is_safe_with_dampener(levels):
        safe_count += 1

print(f"Number of safe reports with Problem Dampener: {safe_count}")
