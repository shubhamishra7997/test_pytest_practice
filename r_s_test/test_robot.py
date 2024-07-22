#Solution:
import pytest

from robot import validate, choose_direction

"""
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
"""

"""
#Validate function
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
        "X.......",
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

#choose direction function

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
    with pytest.raises(Exception, match="Illegal characters found in the provided terrain ({illegal_chars})"):
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
 
# Test cases for choose_direction

def test_choose_direction_no_obstacles():
    terrain = [
        "R.......",
        "........",
        "........",
        "....T...",
        "........",
    ]
    assert choose_direction(terrain) == "S"

def test_choose_direction_with_obstacle():
    terrain = [
        "R.......",
        "####....",
        "....T...",
    ]
    assert choose_direction(terrain) == "E"

def test_choose_direction_edge_case():
    terrain = [
        "R.......",
        "........",
        ".......T",
    ]
    assert choose_direction(terrain) == "E"

def test_choose_direction_unreachable_target():
    terrain = [
        "R#######",
        "########",
        "#######T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_choose_direction_single_cell():
    terrain = [
        "RT"
    ]
    assert choose_direction(terrain) == "E"

def test_choose_direction_north():
    terrain = [
        "....T...",
        "........",
        "........",
        "....R...",
        "........",
    ]
    assert choose_direction(terrain) == "N"

def test_choose_direction_west():
    terrain = [
        "........",
        "........",
        "........",
        "....T...",
        ".....R..",
    ]
    assert choose_direction(terrain) == "W"

def test_choose_direction_west():
    terrain = [
        "........",
        "........",
        "........",
        "........",
        "...T.R..",
    ]
    assert choose_direction(terrain) == "W"
    
def test_choose_direction_large_grid():
    terrain = [
        "R...................",
        "....................",
        "....................",
        "...................T",
    ]
    assert choose_direction(terrain) == "S"

def test_choose_direction_complex_obstacle():
    terrain = [
        "R#########",
        "#........#",
        "#.######.#",
        "#.######.#",
        "#.######.#",
        "#.######.#",
        "#.......T#",
        "##########",
    ]
    assert choose_direction(terrain) == "E"