def sum_part_numbers_in_schematic_from_file(file_path):
    # Function to check if a character is a symbol
    def is_symbol(char):
        return char in "*+-/$@#%=&"

    # Read the schematic from the file
    with open(file_path, "r") as file:
        schematic_lines = file.readlines()

    total_sum = 0
    rows = len(schematic_lines)

    # Iterate through each character in the schematic
    for r in range(rows):
        col = 0
        while col < len(schematic_lines[r]):
            # Check if the current character is a digit
            if schematic_lines[r][col].isdigit():
                # Extract the full number
                number = ""
                while (
                    col < len(schematic_lines[r]) and schematic_lines[r][col].isdigit()
                ):
                    number += schematic_lines[r][col]
                    col += 1

                # Check for adjacent symbols in 8 directions and diagonally
                adjacent_symbol_found = False
                for dr in range(-1, 2):
                    for dc in range(-len(number), 2):
                        nr, nc = r + dr, col - 1 + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < len(schematic_lines[nr])
                            and is_symbol(schematic_lines[nr][nc])
                        ):
                            adjacent_symbol_found = True
                            break
                    if adjacent_symbol_found:
                        break

                # Add the number to the total sum if an adjacent symbol is found
                if adjacent_symbol_found:
                    total_sum += int(number)
            else:
                col += 1

    return total_sum


# Path to the input file
file_path = "input.txt"

# Calculate the sum
print(sum_part_numbers_in_schematic_from_file("input.txt"))
