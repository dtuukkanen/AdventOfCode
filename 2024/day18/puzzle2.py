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


def drop_bytes(grid, bytes):
    start = (0, 0)
    end = (70, 70)
    G = create_graph(grid)
    for byte in bytes:
        x, y = byte
        grid[y][x] = "#"
        G. remove_node((x, y))
        if nx.has_path(G, start, end):
            continue
        else:
            return x, y


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


def main():
    bytes = read_input()
    grid = create_grid()
    print(drop_bytes(grid, bytes))
    

main()
