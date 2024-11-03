coordinates_santa = (0, 0)
coordinates_robosanta = (0, 0)
directions = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}
visited = {coordinates_santa, coordinates_robosanta}

with open("input.txt") as f:
    for index, char in enumerate(f.read().strip()):
        if index % 2 == 0:
            coordinates_santa = tuple(
                sum(x) for x in zip(coordinates_santa, directions[char])
            )
            visited.add(coordinates_santa)
        else:
            coordinates_robosanta = tuple(
                sum(x) for x in zip(coordinates_robosanta, directions[char])
            )
            visited.add(coordinates_robosanta)
print(len(visited))

