vowels = "aeiou"
bad_strings = ["ab", "cd", "pq", "xy"]
nice_strings = 0

with open("input.txt") as file:
    for line in file:
        vowels_count = 0
        double_letter = False
        bad_string = False
        for i in range(len(line) - 1):
            if line[i] in vowels:
                vowels_count += 1
            if line[i] == line[i + 1]:
                double_letter = True
            if line[i:i + 2] in bad_strings:
                bad_string = True

        if vowels_count >= 3 and double_letter and not bad_string:
            nice_strings += 1

print(nice_strings)
