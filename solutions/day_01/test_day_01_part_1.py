from day_01_part_1 import (
    get_total_distance,
    parse_columns,
    parse_line,
    get_distances,
)


example_data = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

example_columns = (
    [3, 4, 2, 1, 3, 3],  # column_a, original order
    [4, 3, 5, 3, 9, 3],  # column_b, original order
)

example_columns_sorted = (
    [1, 2, 3, 3, 3, 4],  # column_a, ascending order
    [3, 3, 3, 4, 5, 9],  # column_b, ascending order
)

example_distances = [1, 1, 3, 2, 6, 0]

# example_total_distance = 1 + 1 + 3 + 2 + 6 + 0
example_total_distance = 11  # sum of distances


def test_parse_line():
    numbers = parse_line("3   4")
    assert numbers == [3, 4]


def test_parse_columns():
    example_lines = example_data.split("\n")
    columns = parse_columns(example_lines)
    assert columns == example_columns


def test_get_distances():
    distances = get_distances(*example_columns)
    assert distances == example_distances


def test_get_total_distance():
    distance = get_total_distance(example_data)
    assert distance == example_total_distance
