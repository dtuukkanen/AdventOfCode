# Inspiration taken from: https://github.com/DownDev/advent-of-code/blob/main/2023/02-1.py


RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

MAX_AMOUNTS = {"red": RED_MAX, "green": GREEN_MAX, "blue": BLUE_MAX}


def read_input():
    with open("input.txt") as f:
        return f.readlines()


def result(lines):
    result = 0

    for line in lines:
        game, sets = line.split(":")
        subsets = sets.split(";")

        game_possibilities = []
        for subset in subsets:
            amounts = {"red": 0, "green": 0, "blue": 0}
            subset = subset.split(",")

            for item in subset:
                amount, color = item.strip().split()
                amounts[color] += int(amount)

            game_possibilities.append(
                all((MAX_AMOUNTS[color] >= amount for color, amount in amounts.items()))
            )

            if (
                amounts["red"] <= 12
                and amounts["green"] <= 13
                and amounts["blue"] <= 14
            ):
                game_possibilities.append(True)
            else:
                game_possibilities.append(False)

        if all(game_possibilities):
            result += int(game.split()[-1])

    return result


def main():
    lines = read_input()
    print(result(lines))


main()
