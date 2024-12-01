from day_01_part_1 import parse_columns
from collections import Counter


def get_total_similarities(data_text: str) -> int:
    """
    Get the Similarity total from a two-column data text file
    """
    lines: list[str] = data_text.split("\n")
    print(f"Read {len(lines):,} total lines")
    column_a, column_b = parse_columns(lines)
    similarities = get_similarities(column_a, column_b)
    return sum(similarities)


def get_similarities(column_a: list[int], column_b: list[int]) -> list[int]:
    """
    Get a list of similarity integers from two equally-sized columns of integers
    """
    similiarities: list[int] = list()
    b_times_appearing: dict[int, int] = Counter()
    assert len(column_a) == len(column_b)
    print(f"column lengths are both {len(column_a):,}")
    for n in column_b:
        b_times_appearing[n] += 1
    print(f"b_times_appearing: {len(b_times_appearing):,} unique values")
    for n in column_a:
        similiarities.append(n * b_times_appearing.get(n, 0))
    nonzero_similarities = [s for s in similiarities if s != 0]
    print(
        f"{len(similiarities):,} similarities, with "
        f"{len(nonzero_similarities):,} non-zero values"
    )
    return similiarities


def get_times_appearing(column: list[int]) -> dict[int, int]:
    """
    Get a mapping of unique numbers -> the number of times they appear
    (from a column, a.k.a. list of integers)
    """
    times_appearing: dict[int, int] = Counter()
    for n in column:
        times_appearing[n] += 1
    return times_appearing


if __name__ == "__main__":

    with open("puzzle_input.txt", "r") as f:
        puzzle_data = f.read()

    total_similiarities = get_total_similarities(puzzle_data)

    print(f"total similarities: {total_similiarities:,} " f"=> {total_similiarities}")
