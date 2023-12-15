def parse_game(game_str):
    game_id, sets_str = game_str.split(": ")
    sets = []
    for set_str in sets_str.split("; "):
        set = {"red": 0, "green": 0, "blue": 0}
        for cube_str in set_str.split(", "):
            count, color = cube_str.split(" ")
            set[color] = int(count)
        sets.append(set)
    return int(game_id.split(" ")[1]), sets


def min_cubes(sets):
    min_set = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        for color in ["red", "green", "blue"]:
            min_set[color] = max(min_set[color], set[color])
    return min_set


def power(set):
    return set["red"] * set["green"] * set["blue"]


def sum_powers():
    sum_powers = 0
    with open("input.txt", "r") as file:
        for game_str in file:
            _, sets = parse_game(game_str.strip())
            min_set = min_cubes(sets)
            sum_powers += power(min_set)
    return sum_powers


print(sum_powers())
