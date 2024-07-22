import pytest
"""
Coding challenges:
In the editor to the right, you are given code for the robot navigation system's validate and choose_direction functions. These functions check whether the provided map's format is valid, and choose the next step toward the robot's target position, respectively.
Your task is to design a set of test scenarios that evaluate the code's functionalities. The code will be executed on the tests you provide, and your score will be based on the number of lines of code executed (code coverage). To earn points, you need to achieve at least 73% code coverage. The more lines your tests cover, the higher the score you will earn. Assume the provided code is correct. You should focus solely on maximizing code coverage.
Each test should be a rectangular grid representing a map, where:
• character . represents an empty cell;
• character # represents an obstacle;
• character R denotes the position of the robot;
• character T denotes the position of the target that the robot needs to reach.
To define a test case, write a function with a name that starts with test_ and returns an array of strings. The number of rows and columns within each test case should be between 1 and 20. You can create at most 20 test cases. If you create more, the 20 tests used for coverage calculation will be chosen at random. Remember to delete the example test if you do not want to use it.
Below you can find an example of how to define a valid test case:
def test_example():
    return [
        "........",
        ".#......",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
 
from collections import deque
 
TARGET = "T"
ROBOT = "R"
OBSTACLE = "#"
all_chars = {".", "T", "R", "#"}
 
INF = float("inf")
 
 
def validate(terrain):
    N, M = len(terrain), len(terrain[0])
    for i in range(N):
        if len(terrain[i]) != M:
            raise Exception("Provided terrain map is not rectangular.")
    used_chars = list("".join(terrain))
    illegal_chars = set(used_chars).difference(all_chars)
    if illegal_chars:
        raise Exception(
            f"Illegal characters found in the provided terrain ({illegal_chars})."
        )
    targets = [(i, j) for i in range(N) for j in range(M) if terrain[i][j] == TARGET]
    robots = [(i, j) for i in range(N) for j in range(M) if terrain[i][j] == ROBOT]
    if len(targets) == 0:
        raise Exception("There is no target.")
    if len(targets) > 1:
        raise Exception("There is more than one target.")
    if len(robots) == 0:
        raise Exception("There is no robot.")
    if len(robots) > 1:
        raise Exception("There is more than one robot.")
    return N, M, targets[0], robots[0]
 
 
def choose_direction(terrain):
    try:
        N, M, target, robot = validate(terrain)
    except Exception as e:
        print(f"An error occured: {e}")
        raise
 
    robot_row, robot_col = robot
 
    def reachable(row, col):
        if 0 <= row < N and 0 <= col < M and terrain[row][col] != OBSTACLE:
            return True
        return False
 
    bfs_queue = deque([target])
    distances = {target: 0}
 
    while len(bfs_queue) and (robot_row, robot_col) not in distances:
        row, col = bfs_queue.popleft()
        for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nrow, ncol = row + drow, col + dcol
            if (nrow, ncol) not in distances:
                if not reachable(nrow, ncol):
                    continue
                distances[(nrow, ncol)] = distances[(row, col)] + 1
                bfs_queue.append((nrow, ncol))
 
    try:
        best_direction, best_distance = None, distances[(robot_row, robot_col)]
    except:
        print(f"An error occured: Target unreachable.")
        raise
 
    if distances.get((robot_row - 1, robot_col), INF) < best_distance:
        best_direction, best_distance = "N", distances[(robot_row - 1, robot_col)]
    if distances.get((robot_row + 1, robot_col), INF) < best_distance:
        best_direction, best_distance = "S", distances[(robot_row + 1, robot_col)]
    if distances.get((robot_row, robot_col - 1), INF) < best_distance:
        best_direction, best_distance = "W", distances[(robot_row, robot_col - 1)]
    if distances.get((robot_row, robot_col + 1), INF) < best_distance:
        best_direction, best_distance = "E", distances[(robot_row, robot_col + 1)]
    return best_direction
 
"""
# write your tests starting each function name with "test_", for example:
def test_example():
    return [
        "........",
        ".#......",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
"""

"""
#from question3 import validate, choose_direction

def test_valid_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
    assert validate(terrain) == (6, 8, (3, 4), (2, 4))

def test_non_rectangular_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T..",
        ".#......",
    ]
    with pytest.raises(Exception, match="Provided terrain map is not rectangular."):
        validate(terrain)

def test_illegal_characters_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..X...",
        ".#..T...",
        "........",
    ]
    with pytest.raises(Exception, match="Illegal characters found in the provided terrain"):
        validate(terrain)

def test_no_target_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#......",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is no target."):
        validate(terrain)

def test_multiple_targets_map():
    terrain = [
        "........",
        ".#......",
        ".#..R.T.",
        ".#..T...",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is more than one target."):
        validate(terrain)

def test_no_robot_map():
    terrain = [
        "........",
        ".#......",
        ".#......",
        ".#..T...",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is no robot."):
        validate(terrain)

def test_multiple_robots_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T.R.",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is more than one robot."):
        validate(terrain)
"""
"""
#Solution:
def test_valid():
    return [
        "...R",
        "T..."
    ]

def test_non_rectangle():
    return [
        "..R",
        "T"
    ]

def test_illegal_char():
    return [
        "..i",
        "e.."
    ]

def test_no_target():
    return [
        "....",
        "...R"
    ]

def test_multiple_target():
    return [
        "T...",
        ".T..",
        "...R"

    ]

def test_no_robot():
    return [
        "T...",
        "....",
        "....",
        "...."
    ]   

def test_multiple_robot():
    return [
        "R....",
        "..R.",
        "...T"
    ]
"""

"""
#old solutions
def test_empty_map():
    return [
        ".R..",
        "...T"
    ]

def test_single_row():
    return [
        "R..T"
    ]
 
def test_single_column():
    return [
        "R",
        ".",
        ".",
        "T"
    ]
 
def test_no_robot():
    try:
        return [
            "...",
            ".T.",
            "..."
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_no_target():
    try:
        return [
            "R..",
            "..."
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_multiple_robots():
    try:
        return [
            "R.R",
            "...",
            "..T"
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_multiple_targets():
    try:
        return [
            "R..",
            ".T.",
            "..T"
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_irregular_map():
    try:
        return [
            "R..",
            "...T",
            "..."
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_illegal_characters():
    try:
        return [
            "R.X.",
            "...T"
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_target_unreachable():
    return [
        "R.#",
        "###",
        "..T"
    ]
 
def test_large_map():
    return [
        "R...................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "...................T"
    ]
 
def test_robot_on_target():
    return [
        "T"
    ]
 
def test_all_obstacles():
    try:
        return [
            "R###",
            "####",
            "###T"
        ]
    except Exception as e:
        print(f"Expected error: {e}")
 
def test_direct_path():
    return [
        "R...",
        ".#..",
        "..#.",
        "...T"
    ]
 
def test_complex_obstacles():
    return [
        "R..#......",
        ".#.#.#....",
        ".#...#....",
        ".#####....",
        "..........",
        "..#####..T"
    ]
 
def test_full_obstacle_row():
    return [
        "R.......",
        "########",
        ".......T"
    ]
 
def test_full_obstacle_column():
    return [
        "R#.....T",
        ".#......",
        ".#......",
        ".#......",
        ".#......"
    ]
 
def test_corner_case():
    return [
        "R.......",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        ".......T"
    ]
 
def test_minimum_map():
    return [
        "RT"
    ]
 
def test_maximum_map():
    return [
        "R...................T",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
        ".....................",
        "####################.",
    ]

def test_diagonal_path():
    return [
        "R......",
        ".#.....",
        "..#....",
        "...#...",
        "....#..",
        ".....#.",
        "......T"
    ]
 
def test_obstacle_around_target():
    return [
        "R.......",
        ".######.",
        ".######.",
        ".######.",
        "....T...",
        ".######.",
        ".######.",
        ".######.",
        "........"
    ]
 
def test_obstacle_around_robot():
    return [
        "....T...",
        ".######.",
        ".######.",
        ".######.",
        ".######.",
        ".######.",
        ".######.",
        ".######.",
        "R......."
    ]
 
def test_robot_adjacent_to_target():
    return [
        "R.T"
    ]
 
def test_robot_and_target_at_opposite_corners():
    return [
        "R.......",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        ".......T"
    ]
 
def test_robot_next_to_obstacle():
    return [
        ".R.",
        ".#.",
        ".T."
    ]
 
def test_single_cell_robot():
    return [
        "R"
    ]
 
def test_single_cell_target():
    return [
        "T"
    ]
 
def test_robot_blocked_in_one_direction():
    return [
        "R#...",
        ".#...",
        "..#..",
        "...#.",
        "....T"
    ]
 
def test_large_open_area():
    return [
        "R...................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        ".................T.."
    ]
 
def test_alternating_obstacles():
    return [
        "R#.#.#.#.#.#.#.#.#.",
        ".#.#.#.#.#.#.#.#.#.",
        "#.#.#.#.#.#.#.#.#.#",
        ".#.#.#.#.#.#.#.#.#.",
        "#.#.#.#.#.#.#.#.#.#",
        ".#.#.#.#.#.#.#.#.#.",
        "#.#.#.#.#.#.#.#.#.#",
        ".#.#.#.#.#.#.#.#.#T"
    ]
 
def test_robot_in_center():
    return [
        "...........",
        "...........",
        "...........",
        "...........",
        "...........",
        ".....R.....",
        "...........",
        "...........",
        "...........",
        "...........",
        "........T.."
    ]
 
def test_target_surrounded_by_obstacles():
    return [
        "R...........",
        "............",
        "............",
        "............",
        "............",
        "............",
        "............",
        "....#####...",
        "....#T#.....",
        "....#####...",
        "............"
    ]
 
def test_all_empty_cells():
    return [
        "R........T"
    ]
 
def test_snake_path():
    return [
        "R#########",
        "#.......#.",
        "#.#####.#.",
        "#.#...#.#.",
        "#.#.###.#.",
        "#.#.....#.",
        "#.#######T"
    ]
 
def test_mixed_obstacles():
    return [
        "R...#....",
        "....#....",
        "..###....",
        "....#....",
        "....#..T.",
        "....#####",
        "........."
    ]
 
def test_dense_obstacles_with_single_path():
    return [
        "R#########",
        "#.......#.",
        "#######.#.",
        "#.....#.#.",
        "#.###.#.#.",
        "#.#...#.#.",
        "#.#####.#.",
        "#.......#T"
    ]
"""	
	
	