from day_04_part_1 import (
    get_rows,
    get_ll_ur_diagonals,
    get_ul_lr_diagonals,
    scan_line,
)
from typing import Iterable
import logging
import sys

log = logging.getLogger("day_04_part_2")


def get_cross_pattern_count(
    text_data: str, patterns: Iterable[str]
) -> int:
    """
    Get the total count of "crossed" patterns in text_data
    """
    none_count = 0
    partial_count = 0
    total_count = 0
    width = len(patterns[0])
    middle = int(width / 2)
    letter = patterns[0][middle]

    rows = get_rows(text_data)
    centers = locate_inner_letters(rows, letter)

    for center in centers:
        subgrid_rows = get_subgrid(rows, center)
        found = scan_diagonals_for_crossed_patterns(subgrid_rows, patterns)
        if found == 2:
            total_count += 1
        elif found == 1:
            partial_count += 1
        else:
            none_count += 1

    log.info("")
    log.info(f"Scanned Diagonals across {len(centers):,} letter {letter}s...")
    log.info(f" * {none_count:,} letter {letter}s have no diagonal patterns")
    log.info(f" * {partial_count:,} letter {letter}s have one diagonal pattern")
    log.info(f" * {total_count:,} letter {letter}s have two crossed patterns!")

    return total_count


def locate_inner_letters(rows: list[str], letter: str):
    """
    Locate x,y coordinates of all instances of letter, within row strings
    (filtering out instances on outer edges or first/last rows)
    """
    log.info("")
    log.info("Locating inner letters...")
    coordinate_pairs = list()
    width = len(rows[0]) - 1
    for y in range(width):
        row = rows[y]
        for x in range(width):
            if row[x] == letter:
                if x > 0 and y > 0 and x < width and y < width:
                    coordinate_pairs.append((x, y))
    log.info(
        f" * Found {len(coordinate_pairs):,} non-edge instances of letter {letter}"
    )
    return coordinate_pairs


def get_subgrid(rows, center):
    """
    Get a 3x3 subgrid, from row strings, given x,y center coordinates
    """
    subgrid = list()
    x, y = center
    for sy in range(y - 1, y + 2):
        row = rows[sy]
        subgrid.append(row[x - 1 : x + 2])
    return subgrid


def scan_diagonals_for_crossed_patterns(rows: Iterable[str], patterns: Iterable[str]):
    """
    Scan diagonals of row strings, return True if both match cross_patterns
    (patterns can be in any order, but must be on diagonals)
    """
    found = 0
    for ll_ur_diagonal in get_ll_ur_diagonals(rows):
        if scan_line(ll_ur_diagonal, patterns):
            found += 1
            break

    for ul_lr_diagonal in get_ul_lr_diagonals(rows):
        if scan_line(ul_lr_diagonal, patterns):
            found += 1
            break

    s = "s" if found != 1 else ""
    found_text = f"Found {found} diagonal pattern{s}"
    success = "YES!" if found == 2 else "nope"
    log.debug("")
    log.debug(rows[0])
    log.debug(f"{rows[1]} {found_text} - {success}")
    log.debug(rows[2])
    return found


if __name__ == "__main__":
    log_level = logging.INFO
    if "-d" in sys.argv:
        log_level = logging.DEBUG
        print("(Detailed Output)")
    else:
        print("(High-level Output: Run with -d for verbose debugging)")

    logging.basicConfig(level=log_level, format="%(message)s")

    # Keep Day 1 logging at INFO
    logging.getLogger("day_04_part_1").setLevel(logging.INFO)

    with open("puzzle_input.txt", "r") as f:
        text_data = f.read()

    MAS = ["MAS", ]

    total_count = get_cross_pattern_count(text_data, MAS)
    print()
    print(f"Total Count: {total_count:,} => {total_count}")
