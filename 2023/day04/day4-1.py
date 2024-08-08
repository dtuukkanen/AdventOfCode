# Open file and read data and split it into rows
with open("input.txt") as f:
    data = f.read().strip().split("\n")

# Result variable
result = 0

# Loop through rows
for row in data:
    # Wins
    wins = 0

    # Split row into winning numbers and my numbers
    winning_numbers, my_numbers = row.split(":")[-1].split("|")
    # Split into numbers
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    # Loop through my numbers and check if they are in winning numbers
    for my_number in my_numbers:
        if my_number in winning_numbers:
            # If there aren't wins yet
            if wins == 0:
                wins += 1
            # If there are wins, double them
            else:
                wins *= 2

    # Add wins to result
    result += wins

print(result)
