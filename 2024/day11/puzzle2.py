from collections import defaultdict

def read_input():
    stones = defaultdict(int)
    with open("input.txt") as f:
        for line in f:
            for stone in map(int, line.split()):
                stones[stone] += 1
    return stones

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        else:
            stone_str = str(stone)
            length = len(stone_str)
            if length % 2 == 0:
                middle = length // 2
                new_stones[int(stone_str[:middle])] += count
                new_stones[int(stone_str[middle:])] += count
            else:
                new_stones[stone * 2024] += count
    return new_stones

def main():
    stones = read_input()
    for _ in range(75):
        stones = blink(stones)
        total_stones = sum(stones.values())
    print(total_stones)

main()