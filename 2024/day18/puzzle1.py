import networkx as nx


def read_input():
    bytes = []
    with open('input.txt') as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            x, y = map(int, line.split(','))
            bytes.append((x, y))
    return bytes


def create_grid():
    grid = [["." for i in range(71)] for j in range(71)]
    return grid


def drop_bytes(grid, bytes, amount):
    for i in range(amount):
        x, y = bytes[i]
        grid[y][x] = "#"
    return grid


def create_graph(grid):
    # Create graph from only elements of . that are connected by being in the same row or column not diagonally
    G = nx.Graph()
    for i in range(71):
        for j in range(71):
            if grid[i][j] == ".":
                G.add_node((i, j))
                if i > 0 and grid[i - 1][j] == ".": # Up
                    G.add_edge((i, j), (i - 1, j))
                if j > 0 and grid[i][j - 1] == ".": # Left
                    G.add_edge((i, j), (i, j - 1))
                if i < 70 and grid[i + 1][j] == ".": # Down
                    G.add_edge((i, j), (i + 1, j))
                if j < 70 and grid[i][j + 1] == ".": # Right
                    G.add_edge((i, j), (i, j + 1))
    return G


def draw_path(grid, path):
    for i in range(len(path)):
        x, y = path[i]
        grid[y][x] = "O"
    return grid


def draw_grid(grid):
    for i in range(71):
        for j in range(71):
            print(grid[i][j], end="")
        print()


def main():
    start = (0, 0)
    end = (70, 70)
    bytes = read_input()
    grid = create_grid()
    grid = drop_bytes(grid, bytes, 1024)
    G = create_graph(grid)
    print(nx.shortest_path_length(G, source=start, target=end))
    

main()
