import random
from problem_functions import *
# imported this way, just to indicate that we are using a search algorithm function when we do so.
import search_algorithms


def print_grid(grid, goal_index):
    text_array = []
    for cell in grid:
        if (cell == 0):
            text_array.append("      ")
        elif cell == 1:
            text_array.append("<o^^o>")
        elif cell == -1:
            text_array.append("XXXXXX")
    text_array[goal_index] = " GOAL "

    print(
        '-'*37 + '\n' +
        '| ' + text_array[0] + ' | ' + text_array[1] + ' | ' + text_array[2] + ' | ' + text_array[3] + ' |' + '\n' +
        '-'*37 + '\n' +
        '| ' + text_array[4] + ' | ' + text_array[5] + ' | ' + text_array[6] + ' | ' + text_array[7] + ' |' + '\n' +
        '-'*37 + '\n' +
        '| ' + text_array[8] + ' | ' + text_array[9] + ' | ' + text_array[10] + ' | ' + text_array[11] + ' |' + '\n' +
        '-'*37 + '\n' +
        '| ' + text_array[12] + ' | ' + text_array[13] + ' | ' + text_array[14] + ' | ' + text_array[15] + ' |' + '\n' +
        '-'*37
    )


def setup_grid(random_factor):
    grid = [0]*16
    goal_index, car_position, no_blocks = 0, 0, 0
    for _ in range(random_factor):
        while goal_index == car_position:
            goal_index = random.randint(0, len(grid)-1)
            car_position = random.randint(0, len(grid)-1)
        no_blocks = random.randint(0, 5)

    grid[car_position] = 1

    for _ in range(no_blocks):
        rnd = random.randint(0, len(grid)-1)
        # adding >>>  or grid[rnd] == -1 which prevents block overwrite
        while rnd == goal_index or rnd == car_position:
            rnd = random.randint(0, len(grid)-1)
        grid[rnd] = -1

    return grid, goal_index


def human_solve(grid, goal_index):
    grid = grid[:]  # not necessary
    steps_counter = 0
    while (True):
        print_grid(grid, goal_index)
        available_actions = generate_actions(grid)
        print('Available Actions: ' + ' , '.join(available_actions))
        action = input("YOUR ACTION: ")
        if action not in available_actions:
            print('Game Over!')
            return
        grid = apply_action(grid, action)
        steps_counter += 1

        if check_grid(grid, goal_index):
            print_grid(grid, goal_index)
            print("You won!")
            print("Steps: ", steps_counter)
            return


def computer_solve(strategy, grid, goal_index, h=None, show_details=False):
    S = search_algorithms.solve(
        strategy, grid, goal_index, generate_actions, apply_action, check_grid, move_cost, h)

    if S == 'failure':
        print('failed!')
        return

    print(strategy)
    for i in S:
        print(i, ": ", S[i])
    print('-'*50)

    if show_details:
        grid = grid[:]  # not necessary
        print_grid(grid, goal_index)

        for action in S['solution']:
            grid = apply_action(grid, action)
            print_grid(grid, goal_index)


# Initializing the problem
grid, goal = setup_grid(100)

# Solve for yourself:
# human_solve(grid,goal)

# Let AI do the job!
computer_solve('Astar', grid, goal, h=h2, show_details=True)

# More examples to use:
#   'BFS', grid, goal, show_details = True
#   'DFS', grid, goal, show_details = True
#   'UCS', grid, goal, show_details = True

#   'Greedy', grid, goal, h = h2, show_details = True
#   'Astar', grid, goal, h = h2, show_details = True

# print_grid(grid,goal)
