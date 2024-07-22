import pytest
from question3 import choose_direction, validate

def test_scenario_multiple_obstacles():
    terrain = [
        "R.......",
        "........",
        "....#...",
        "....#...",
        "....#...",
        "....#...",
        "........",
        ".......T",
    ]
    assert choose_direction(terrain) == "E"

def test_large_map_no_obstacles():
    terrain = [
        "R..................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "..................T",
    ]
    assert choose_direction(terrain) == "E"

def test_narrow_path():
    terrain = [
        "R.................",
        "#################.",
        "................T.",
    ]
    assert choose_direction(terrain) == "S"

def test_l_shaped_obstacle():
    terrain = [
        "R....",
        "#####",
        "...T.",
        ".....",
    ]
    assert choose_direction(terrain) == "S"

def test_u_shaped_obstacle():
    terrain = [
        "R........",
        "#####....",
        "#...#....",
        "#...#####",
        "#.......T",
    ]
    assert choose_direction(terrain) == "S"

def test_robot_next_to_target_blocked():
    terrain = [
        "R#",
        "#T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_minimum_size_map_no_path():
    terrain = [
        "R#T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_maximum_size_map_no_path():
    terrain = [
        "R..................",
        "###################",
        "..................T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_unreachable_target_complex():
    terrain = [
        "R....",
        "#####",
        "...#.",
        "...#.",
        "...#T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_multiple_paths():
    terrain = [
        "R.......",
        "........",
        "....#...",
        "....#...",
        "....#...",
        "....#...",
        "........",
        ".......T",
    ]
    assert choose_direction(terrain) in {"S", "E"}

def test_diagonal_blocked():
    terrain = [
        "R#...",
        ".#...",
        "..#..",
        "...#.",
        "....T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)
        
def test_valid_scenario_1():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
    assert choose_direction(terrain) in {"N", "S"}

def test_valid_scenario_2():
    terrain = [
        "R.......",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        ".......T",
    ]
    assert choose_direction(terrain) == "S"

def test_valid_scenario_3():
    terrain = [
        "R.......",
        "........",
        "...#....",
        "...#....",
        "...#....",
        "...#....",
        "........",
        ".......T",
    ]
    assert choose_direction(terrain) == "S"

def test_no_robot():
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

def test_no_target():
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

def test_multiple_robots():
    terrain = [
        "........",
        ".#..R...",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is more than one robot."):
        validate(terrain)

def test_multiple_targets():
    terrain = [
        "........",
        ".#..R...",
        ".#..T...",
        ".#..T...",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="There is more than one target."):
        validate(terrain)

def test_non_rectangular_map():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T..",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="Provided terrain map is not rectangular."):
        validate(terrain)

def test_illegal_characters():
    terrain = [
        "........",
        ".#......",
        ".#.R....",
        ".#.T....",
        ".#......",
        "........",
    ]
    with pytest.raises(Exception, match="Illegal characters found in the provided terrain"):
        validate(terrain)

def test_unreachable_target():
    terrain = [
        "R.......",
        "########",
        "........",
        "........",
        "........",
        "........",
        "........",
        ".......T",
    ]
    with pytest.raises(Exception, match="Target unreachable."):
        choose_direction(terrain)

def test_target_adjacent_north():
    terrain = [
        "........",
        ".#......",
        ".#..T...",
        ".#..R...",
        ".#......",
        "........",
    ]
    assert choose_direction(terrain) == "N"

def test_target_adjacent_south():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#..T...",
        ".#......",
        "........",
    ]
    assert choose_direction(terrain) == "S"

def test_target_adjacent_west():
    terrain = [
        "........",
        ".#......",
        ".#..T...",
        ".#R.....",
        ".#......",
        "........",
    ]
    assert choose_direction(terrain) == "W"

def test_target_adjacent_east():
    terrain = [
        "........",
        ".#......",
        ".#..R...",
        ".#.T....",
        ".#......",
        "........",
    ]
    assert choose_direction(terrain) == "E"

def test_minimum_size_map():
    terrain = ["RT"]
    assert choose_direction(terrain) == "E"

def test_single_row_map():
    terrain = ["R.......T"]
    assert choose_direction(terrain) == "E"

def test_single_column_map():
    terrain = [
        "R",
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        "T",
    ]
    assert choose_direction(terrain) == "S"

def test_maximum_size_map():
    terrain = [
        "R..................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "...................",
        "..................T",
    ]
    assert choose_direction(terrain) == "E"

if __name__ == "__main__":
    pytest.main()