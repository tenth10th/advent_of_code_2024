import string


def get_total_distance(data_text: str) -> int:
    """
    Get the Distance total from a two-column data text file
    """
    lines = data_text.split("\n")
    column_a, column_b = parse_columns(lines)
    assert len(column_a) == len(column_b), "Columns are of equal lengths"
    print(f"Read {len(lines):,} total lines")

    column_a.sort()
    column_b.sort()
    print("(Sorted both columns, ascending order)")
    print(f"Parsed 2 columns of {len(column_a):,} integers")

    distances = get_distances(column_a, column_b)
    nzds = [d for d in distances if d > 0]
    print(f"(found {len(nzds):,} non-zero distances)")

    total_distance = sum(distances)
    return total_distance


def parse_line(line: str) -> list[int]:
    """
    Parse integers from a whitespace-delimited line of text
    e.g. "23   42" becomes [23, 42]
    """
    digits: list[str] = list()
    numbers: list[int] = list()
    for c in line:
        if c in string.whitespace:
            if digits:
                numbers.append(int("".join(digits)))
            digits = []
        else:
            digits.append(c)
    if digits:
        numbers.append(int("".join(digits)))
    return numbers


def parse_columns(data_lines: list[str], debug=False) -> tuple[list[int], list[int]]:
    """
    Turn a vertical, two-column, whitespace-delimited text file into two lists of integers
    (see test_day_01_part_1.py for example data)

    (Prints verbose intermediate states if debug is set to True)
    """
    column_a, column_b = list(), list()
    for line in data_lines:
        numbers = parse_line(line)
        if not numbers:
            continue
        if debug:
            print(f"Line: {line}")
            print(f"Numbers: {numbers}")
        column_a.append(numbers[0])
        column_b.append(numbers[1])

    return column_a, column_b


def get_distances(column_a, column_b):
    """
    Get list of (absolute) distances between the values of two equally-sized lists of integers
    """
    distances = list()
    for i in range(len(column_a)):
        distances.append(abs(column_a[i] - column_b[i]))
    return distances


if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as f:
        puzzle_data = f.read()

    total_distance = get_total_distance(puzzle_data)

    print(f"total distance: {total_distance:,} => {total_distance}")
