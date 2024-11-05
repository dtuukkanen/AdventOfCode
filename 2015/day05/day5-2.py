nice_strings = 0

with open("input.txt") as file:
    for line in file:
        pair_repeats = False
        repeat_with_space = False
        for i in range(len(line) - 2):
            if line.count(line[i:i + 2]) >= 2:
                pair_repeats = True
            if line[i] == line[i + 2]:
                repeat_with_space = True
        
        if pair_repeats and repeat_with_space:
            nice_strings += 1
print(nice_strings)
