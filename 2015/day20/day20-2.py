def sum_of_presents(house):
    total = 0
    # Only iterate up to square root
    for elf in range(1, int(house ** 0.5) + 1):
        if house % elf == 0:
            # Small divisor (elf)
            if house <= elf * 50:
                total += elf * 11
            
            # Larger paired divisor
            paired_elf = house // elf
            if elf != paired_elf:  # Avoid counting square roots twice
                if house <= paired_elf * 50:
                    total += paired_elf * 11
    return total

# Start from a reasonable number based on input
house = 700000  # We can start higher since part 2 gives more presents
while True:
    presents = sum_of_presents(house)
    if presents >= 36000000:
        print(f"House {house} gets {presents} presents")
        break
    house += 1