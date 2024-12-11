def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            stones = list(map(int, line.split(" ")))
    return stones

def blink(stones):
    new = []

    for i in range(len(stones)):
        stone = stones[i]
        if stone == 0:
            new.append(1)
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            stone1 = int(str(stone)[:middle])
            stone2 = int(str(stone)[middle:])
            new.append(stone1)
            new.append(stone2)
        else:
            new.append(stone * 2024)
    
    return new

def main():
    stones = read_input()
    for _ in range(25):
        stones = blink(stones)
    print(len(stones))

main()