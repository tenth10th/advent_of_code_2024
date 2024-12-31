import logging
import sys
from typing import Iterable

log = logging.getLogger("day_04_part_1")

XMAS = ("XMAS",)


def get_pattern_count(text_data: str, patterns: Iterable[str] = XMAS) -> str:
    total_count = 0
    in_rows_count = 0
    in_columns_count = 0
    in_ll_ur_count = 0
    in_ul_lr_count = 0

    rows = get_rows(text_data)
    for row in rows:
        in_rows_count += scan_line(row, patterns)
    total_count += in_rows_count
    print(f"Processed {len(rows)} Rows, containing {in_rows_count:,} patterns")

    columns = get_columns(text_data)
    for column in columns:
        in_columns_count += scan_line(column, patterns)
    total_count += in_columns_count
    print(f"Processed {len(columns)} Columns, containing {in_columns_count:,} patterns")

    ll_ur_diagonals = get_ll_ur_diagonals(rows)
    for ll_ur_diagonal in ll_ur_diagonals:
        in_ll_ur_count += scan_line(ll_ur_diagonal, patterns)
    total_count += in_ll_ur_count
    print(f"Processed {len(ll_ur_diagonals)} LL/UR Diagonals, containing {in_ll_ur_count:,} patterns")

    ul_lr_diagonals = get_ul_lr_diagonals(rows)
    for ul_lr_diagonal in ul_lr_diagonals:
        in_ul_lr_count += scan_line(ul_lr_diagonal, patterns)
    total_count += in_ul_lr_count
    print(f"Processed {len(ul_lr_diagonals)} UL/LR Diagonals, containing {in_ul_lr_count:,} patterns")

    return total_count


def scan_line(line: str, patterns: Iterable[str]) -> int:
    all_patterns = get_all_patterns(patterns)
    found_count = 0
    log.debug(f"Scanning: {line}")
    for pattern in all_patterns:
        start = 0
        all_pos = list()
        pos = line.find(pattern, start)
        while pos != -1:
            all_pos.append(pos)
            found_count += 1
            start = pos + 1
            if start > len(line):
                pos = -1
            else:
                pos = line.find(pattern, start)
        if all_pos:
            positions = ", ".join([str(pos) for pos in all_pos])
            log.debug(f"   (Found {pattern} at {positions})")
    return found_count


def get_all_patterns(patterns: Iterable[str]) -> list[str]:
    """
    Return list of variants of patterns (currently, forwards/backwards)
    """
    all_patterns = []
    for pattern in patterns:
        all_patterns.append(pattern)
        all_patterns.append("".join(reversed(pattern)))
    return all_patterns


def get_rows(text_data: str) -> list[str]:
    """
    Extract a list of rows from text (breaking on \n)
    """
    lines = list()
    for line in text_data.split("\n"):
        clean_line = line.strip()
        if clean_line:
            lines.append(clean_line)
    return lines


def get_columns(text_data) -> list[str]:
    """
    Extract a list of columns from text (based on \n rows)
    """
    columns = list()
    rows = get_rows(text_data)
    row_len = len(rows[0])
    for i in range(row_len):
        col_chars = list()
        for row in rows:
            col_chars.append(row[i])
        column = "".join(col_chars)
        columns.append(column)
    return columns


def get_diag_range(
    rows: list[str],
    start_x: int = None,
    start_y: int = None,
    sxd: int = 0,
    syd: int = 0,
    xd: int = 1,
    yd: int = 1,
) -> list[str]:
    """
    Extract all diagonals from a list of row strings, given:
    * starting x and y coords (defaults to row width)
    * starting x and y deltas (defaults to 0)
    * x and y deltas (defaults to 1)
    Starting from start_x and start_y:
    Attempt the following (width) times:
    * Set x at start_x, y at start_y
    * Increment x by xd, y and yd
    * (until x or y exit the bounds of >= 0, < width)
    * Increment start_x by sxd, start_y by syd
    """
    diagonals = list()
    width = len(rows[0])
    if start_x is None:
        start_x = width - 1
    if start_y is None:
        start_y = width - 1
    for _ in range(width):
        x = start_x
        y = start_y
        diag_chars = list()
        coords = list()
        while x < width and y < width and x >= 0 and y >= 0:
            dchar = rows[y][x]
            diag_chars.append(dchar)
            coords.append(f"{x},{y}")
            x += xd
            y += yd
        start_x += sxd
        start_y += syd
        if diag_chars:
            diagonal = "".join(diag_chars)
            coordinates = " ".join(coords)
            log.debug(f"Diagonal: {coordinates} -> {diagonal}")
            diagonals.append(diagonal)
    return diagonals


"""
ABC
DEF
GHI

0,0
1,0 0,1
2,0 1,1 0,2
2,1 1,2
2,2
"""


def get_ll_ur_diagonals(rows: list[str]) -> list[str]:
    """
    Generate the lower-left to upper-right diagonals for given list of row strings
    (as a new list of strings)
    """
    diagonals = list()
    diagonals += get_diag_range(rows, start_x=0, start_y=0, sxd=1, xd=-1)
    diagonals += get_diag_range(rows, start_y=1, syd=1, xd=-1)
    return diagonals


"""
ABC
DEF
GHI

2,0
1,0 2,1
0,0 1,1 2,2
0,1 1,2
0,2
"""


def get_ul_lr_diagonals(rows: list[str]) -> list[str]:
    """
    Generate the upper-left to lower-right diagonals for given list of row strings
    (as a new list of strings)
    """
    diagonals = list()
    diagonals += get_diag_range(rows, start_y=0, sxd=-1)
    diagonals += get_diag_range(rows, start_x=0, start_y=1, syd=1)
    return diagonals


if __name__ == "__main__":

    log_level = logging.INFO
    if "-d" in sys.argv:
        log_level = logging.DEBUG
        print("(Detailed Output)")
    else:
        print("(High-level Output: Run with -d for verbose debugging)")

    logging.basicConfig(level=log_level, format="%(message)s")

    with open("puzzle_input.txt", "r") as f:
        text_data = f.read()

    total_count = get_pattern_count(text_data, patterns=XMAS)

    print(f"Total Pattern Count: {total_count:,} => {total_count}")
