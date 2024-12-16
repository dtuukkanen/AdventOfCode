import networkx as nx
from enum import Enum
from collections import defaultdict

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def read_input():
    with open('input.txt') as file:
        return [list(line.strip()) for line in file]

def get_turn_cost(current_dir, next_dir):
    diff = abs(current_dir.value - next_dir.value)
    return 0 if diff == 0 else 1000

def create_graph(matrix):
    graph = nx.DiGraph()
    start = end = None
    rows, cols = len(matrix), len(matrix[0])

    # Create nodes and edges
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '#':
                for current_dir in Direction:
                    curr_node = (i, j, current_dir)
                    graph.add_node(curr_node)
                    
                    # Add turning edges
                    for next_dir in Direction:
                        if current_dir != next_dir:
                            graph.add_edge(curr_node, (i, j, next_dir), 
                                         weight=get_turn_cost(current_dir, next_dir))
                    
                    # Add forward movement edges
                    ni, nj = get_next_position(i, j, current_dir)
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] != '#':
                        graph.add_edge(curr_node, (ni, nj, current_dir), weight=1)

                if matrix[i][j] == 'S':
                    start = (i, j, Direction.EAST)
                elif matrix[i][j] == 'E':
                    end = (i, j)

    return graph, start, end

def get_next_position(i, j, direction):
    if direction == Direction.NORTH: return (i-1, j)
    if direction == Direction.SOUTH: return (i+1, j)
    if direction == Direction.EAST: return (i, j+1)
    if direction == Direction.WEST: return (i, j-1)

def find_optimal_paths(graph, start, end):
    min_cost = float('inf')
    all_optimal_paths = []
    
    for end_dir in Direction:
        end_node = (end[0], end[1], end_dir)
        try:
            cost = nx.shortest_path_length(graph, start, end_node, weight='weight')
            if cost < min_cost:
                min_cost = cost
                all_optimal_paths = []
            if cost == min_cost:
                # Get ALL shortest paths to this end direction
                paths = list(nx.all_shortest_paths(graph, start, end_node, weight='weight'))
                all_optimal_paths.extend(paths)
        except nx.NetworkXNoPath:
            continue
    
    return all_optimal_paths, min_cost

def get_unique_tiles(optimal_paths):
    unique_tiles = set()
    for path in optimal_paths:
        for node in path:
            unique_tiles.add((node[0], node[1]))
    return unique_tiles

def validate_paths(graph, paths):
    costs = [nx.path_weight(graph, path, weight='weight') for path in paths]
    return all(cost == costs[0] for cost in costs)

def main():
    matrix = read_input()
    graph, start, end = create_graph(matrix)
    optimal_paths, min_cost = find_optimal_paths(graph, start, end)
    
    # Validate paths have same cost
    if not validate_paths(graph, optimal_paths):
        print("Warning: Not all paths have same cost!")
    
    unique_tiles = get_unique_tiles(optimal_paths)
    print(f"Number of unique tiles in optimal paths: {len(unique_tiles)}")
    print(f"Minimum cost: {min_cost}")
    print(f"Number of optimal paths found: {len(optimal_paths)}")


if __name__ == "__main__":
    main()