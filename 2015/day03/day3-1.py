coordinates = (0, 0)
directions = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}
visited = {coordinates}

with open("input.txt") as f:
    for char in f.read().strip():
        coordinates = tuple(
            sum(x) for x in zip(coordinates, directions[char])
        )
        visited.add(coordinates)
print(len(visited))

