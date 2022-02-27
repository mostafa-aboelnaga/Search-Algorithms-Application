def get_car_position(grid):
    for i in range(len(grid)):
        if grid[i] == 1:
            return i


def generate_actions(grid):
    car_position = get_car_position(grid)
    actions = []
    if car_position not in [0, 1, 2, 3] and grid[car_position-4] != -1:
        actions.append('^')
    if car_position not in [12, 13, 14, 15] and grid[car_position+4] != -1:
        actions.append('v')
    if car_position not in [3, 7, 11, 15] and grid[car_position+1] != -1:
        actions.append('>')
    if car_position not in [0, 4, 8, 12] and grid[car_position-1] != -1:
        actions.append('<')
    return actions


def apply_action(old_grid, action):
    grid = old_grid[:]
    car_position = get_car_position(grid)
    if action == '>':
        grid[car_position], grid[car_position +
                                 1] = grid[car_position+1], grid[car_position]
    if action == '<':
        grid[car_position], grid[car_position -
                                 1] = grid[car_position-1], grid[car_position]
    if action == '^':
        grid[car_position], grid[car_position -
                                 4] = grid[car_position-4], grid[car_position]
    if action == 'v':
        grid[car_position], grid[car_position +
                                 4] = grid[car_position+4], grid[car_position]
    return grid


def check_grid(grid, goal_index):
    return get_car_position(grid) == goal_index


def move_cost(direction, action):
    if action == direction:
        return 1
    else:
        return 2


def h1(grid, goal_index):  # Inadmissible
    car_position = get_car_position(grid)
    return abs(goal_index - car_position)


def h2(grid, goal_index):  # Admissible, meaning that:  h <= actual cost
    car_position = get_car_position(grid)

    car_row = int(car_position / 4)
    car_col = int(car_position % 4)

    goal_row = int(goal_index / 4)
    goal_col = int(goal_index % 4)

    steps = abs(car_row - goal_row) + abs(car_col - goal_col)
    return steps
