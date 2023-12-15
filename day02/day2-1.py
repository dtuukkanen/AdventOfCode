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


def is_possible(sets):
    for set in sets:
        if set["red"] > 12 or set["green"] > 13 or set["blue"] > 14:
            return False
    return True


def sum_possible_ids():
    sum_ids = 0
    with open("input.txt", "r") as file:
        for game_str in file:
            game_id, sets = parse_game(game_str.strip())
            if is_possible(sets):
                sum_ids += game_id
    return sum_ids


print(sum_possible_ids())
