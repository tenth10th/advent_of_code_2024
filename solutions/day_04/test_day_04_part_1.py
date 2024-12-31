from day_04_part_1 import (
    get_pattern_count,
    scan_line,
    get_all_patterns,
    get_rows,
    get_columns,
    get_ll_ur_diagonals,
    get_ul_lr_diagonals,
    XMAS,
)
import pytest


example_data = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

small_example_data = """\
ABC
DEF
GHI
"""


def test_get_xmas_count():
    xmas_count = get_pattern_count(example_data, patterns=XMAS)
    assert xmas_count == 18


def test_get_all_patterns():
    all_patterns = get_all_patterns(
        [
            "XMAS",
        ]
    )
    assert all_patterns == ["XMAS", "SAMX"]


@pytest.mark.parametrize(
    "line, expected_count",
    [
        ("XMAS", 1),
        ("SAMX", 1),
        ("XMASXMAS", 2),
        ("XMASAMX", 2),
        ("SAMXMAS", 2),
        ("XMASXMASSAMXXMAS", 4),
        ("XMAS XMAS SAMXMAS", 4),
    ],
)
def test_scan_line(line: str, expected_count: int):
    assert scan_line(line, patterns=XMAS) == expected_count


def test_get_rows():
    rows = get_rows(small_example_data)
    assert rows == [
        "ABC",
        "DEF",
        "GHI",
    ]


def test_get_columns():
    columns = get_columns(small_example_data)
    assert columns == [
        "ADG",
        "BEH",
        "CFI",
    ]


def test_get_ll_ur_diagonals():
    rows = get_rows(small_example_data)
    diagonals = get_ll_ur_diagonals(rows)
    assert diagonals == [
        "A",
        "BD",
        "CEG",
        "FH",
        "I",
    ]


def test_get_ul_lr_diagonals():
    rows = get_rows(small_example_data)
    diagonals = get_ul_lr_diagonals(rows)
    assert diagonals == [
        "C",
        "BF",
        "AEI",
        "DH",
        "G",
    ]
