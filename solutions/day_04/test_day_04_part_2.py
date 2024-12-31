from day_04_part_2 import (
    get_cross_pattern_count,
    locate_inner_letters,
    get_rows,
    get_subgrid,
    scan_diagonals_for_crossed_patterns,
)
from test_day_04_part_1 import example_data, small_example_data
import pytest

"""
ABC
DEF
GHI
"""


def test_get_cross_pattern_count():
    total_count = get_cross_pattern_count(example_data, patterns=("MAS"))
    assert total_count == 9


small_rows = get_rows(small_example_data)


@pytest.mark.parametrize(
    "rows,letter,expected_locations",
    [
        (small_rows, "A", []),
        (small_rows, "B", []),
        (small_rows, "C", []),
        (small_rows, "C", []),
        (small_rows, "E", [(1, 1)]),
        (small_rows, "F", []),
        (small_rows, "G", []),
        (small_rows, "H", []),
        (small_rows, "I", []),
    ],
    ids=lambda x: str(x[0]) if isinstance(x, str) or len(x) == 1 else "",
)
def test_locate_letters(rows, letter, expected_locations):
    """
    (In small_example_data, ABCDFGHI are on edges, but E is not)
    """
    locations = locate_inner_letters(rows, letter)
    assert locations == expected_locations


def test_get_subgrid():
    rows = get_rows(example_data)
    center = (2, 1)
    subgrid = get_subgrid(rows, center)
    assert subgrid == [
        "MMS",
        "SAM",
        "MXS",
    ]


@pytest.mark.parametrize("subgrid, expected_count", [
    ([
        "MMS",
        "SAM",
        "MXS",
    ], 1),
    ([
        "SMS",
        "SAM",
        "MXS",
    ], 0),
])
def test_scan_diagonals_for_crossed_patterns(subgrid, expected_count):
    cross_count = scan_diagonals_for_crossed_patterns(subgrid, patterns=("MAS", ))
    assert cross_count == expected_count
