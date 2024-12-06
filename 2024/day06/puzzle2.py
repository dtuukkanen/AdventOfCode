def create_matrix():
    with open("input.txt") as f:
        data = f.readlines()
        matrix = []
        for line in data:
            line = line.strip()
            matrix.append(list(line))
    return matrix

def simulate_with_obstacle(grid, start_pos, start_dir, obstacle_pos):
    # Make a copy of the grid and place the new obstacle
    new_grid = [list(row) for row in grid]
    new_grid[obstacle_pos[0]][obstacle_pos[1]] = '#'

    # Directions: up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = {'^': 0, '>': 1, 'v': 2, '<': 3}

    pos = start_pos
    d = dir_idx[start_dir]
    visited_states = set()

    while True:
        # Check if state has been seen before (loop detected)
        state = (pos[0], pos[1], d)
        if state in visited_states:
            return True  # Loop found
        visited_states.add(state)

        # Check next position
        next_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])

        # If next position is obstacle, turn right
        if new_grid[next_pos[0]][next_pos[1]] == '#':
            d = (d + 1) % 4
        else:
            # Move forward
            pos = next_pos
            # Check if guard left the map
            if (pos[0] == 0 or pos[0] == len(new_grid)-1 or
                pos[1] == 0 or pos[1] == len(new_grid[0])-1):
                return False  # No loop found

def count_loop_positions(grid):
    # Find starting position and direction
    start_pos = None
    start_dir = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in '^>v<':
                start_pos = (i, j)
                start_dir = grid[i][j]
                break
        if start_pos:
            break

    # Try each empty position
    loop_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (i, j) != start_pos:
                if simulate_with_obstacle(grid, start_pos, start_dir, (i, j)):
                    loop_count += 1

    return loop_count

def main():
    grid = create_matrix()
    print(count_loop_positions(grid))

if __name__ == '__main__':
    main()
