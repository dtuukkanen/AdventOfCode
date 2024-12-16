import networkx as nx
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def read_input():
    matrix = []
    with open('input.txt') as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def get_turn_cost(current_dir, next_dir):
    diff = abs(current_dir.value - next_dir.value)
    if diff == 0:
        return 0
    return 1000  # Cost for 90-degree turn

def create_graph(matrix):
    graph = nx.DiGraph()
    start = end = None

    # Create nodes for each position and direction
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '#':
                for direction in Direction:
                    graph.add_node((i, j, direction))
                if matrix[i][j] == 'S':
                    start = (i, j, Direction.EAST)
                elif matrix[i][j] == 'E':
                    end = (i, j, Direction.EAST)

    # Add edges with weights
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                continue
                
            for current_dir in Direction:
                # Add turning edges at current position
                for next_dir in Direction:
                    if current_dir != next_dir:
                        graph.add_edge((i, j, current_dir), 
                                     (i, j, next_dir), 
                                     weight=get_turn_cost(current_dir, next_dir))
                
                # Add forward movement edge
                ni, nj = i, j
                if current_dir == Direction.NORTH: ni -= 1
                elif current_dir == Direction.SOUTH: ni += 1
                elif current_dir == Direction.EAST: nj += 1
                elif current_dir == Direction.WEST: nj -= 1
                
                if (0 <= ni < len(matrix) and 
                    0 <= nj < len(matrix[0]) and 
                    matrix[ni][nj] != '#'):
                    graph.add_edge((i, j, current_dir), 
                                 (ni, nj, current_dir), 
                                 weight=1)

    return graph, start, end

def main():
    matrix = read_input()
    graph, start, end = create_graph(matrix)
    
    # Find shortest path considering all possible ending directions
    min_cost = float('inf')
    for direction in Direction:
        try:
            cost = nx.shortest_path_length(graph, start, 
                                         (end[0], end[1], direction), 
                                         weight='weight')
            min_cost = min(min_cost, cost)
        except nx.NetworkXNoPath:
            continue
            
    print(min_cost)

if __name__ == "__main__":
    main()