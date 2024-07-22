"""
In the code below, you are given code for the robot navigation system's validate and choose_direction functions. 
These functions check whether the provided map's format is valid, and choose the next step toward the 
robot's target position, respectively.
Your task is to design a set of test scenarios that evaluate the code's functionalities. 
The code will be executed on the tests you provide, and your score will be based on the 
number of lines of code executed (code coverage). To earn points, you need to achieve at least 73% code coverage. 
The more lines your tests cover, the higher the score you will earn. Assume the provided code is correct. 
You should focus solely on maximizing code coverage.
Each test should be a rectangular grid representing a map, where:
	•	character . represents an empty cell;
	•	character # represents an obstacle;
	•	character R denotes the position of the robot;
	•	character T denotes the position of the target that the robot needs to reach.
To define a test case, write a function with a name that starts with test_ and returns an array of strings. 
The number of rows and columns within each test case should be between 1 and 20. 
You can create at most 20 test cases. 
If you create more, the 20 tests used for coverage calculation will be chosen at random. 
Remember to delete the example test if you do not want to use it.
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
        print(f"An error occurred: {e}")
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
    except KeyError:
        print(f"An error occurred: Target unreachable.")
        raise Exception("Target unreachable.")

    if distances.get((robot_row - 1, robot_col), INF) < best_distance:
        best_direction, best_distance = "N", distances[(robot_row - 1, robot_col)]
    if distances.get((robot_row + 1, robot_col), INF) < best_distance:
        best_direction, best_distance = "S", distances[(robot_row + 1, robot_col)]
    if distances.get((robot_row, robot_col - 1), INF) < best_distance:
        best_direction, best_distance = "W", distances[(robot_row, robot_col - 1)]
    if distances.get((robot_row, robot_col + 1), INF) < best_distance:
        best_direction, best_distance = "E", distances[(robot_row, robot_col + 1)]
    return best_direction