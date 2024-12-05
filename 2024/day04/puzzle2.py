def diagonal(data):
    found = 0

    # Find A
    for row in range(1, len(data) - 1):
        for column in range(1, len(data[0]) - 1):
            if data[row][column] == "A":
                # Save letters from corners
                top_left = data[row-1][column-1]
                top_right = data[row-1][column+1]
                bottom_left = data[row+1][column-1]
                bottom_right = data[row+1][column+1]

                # Check if corners are M and S
                left_side = (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")
                right_side = (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M")

                # If both sides are correct, there must be X-MAS. So found +1
                if left_side and right_side:
                    found += 1

    return found

def main():
    found = 0
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = [row.strip() for row in data]
        found += diagonal(data)

    print(found)

main()
