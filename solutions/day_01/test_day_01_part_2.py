from day_01_part_2 import get_similarities, get_total_similarities


example_data = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

example_columns = (
    [3, 4, 2, 1, 3, 3],  # column_a
    [4, 3, 5, 3, 9, 3],  # column_b
)

# Pairs of {number: times_appearing}
expected_b_times_appearing = {3: 3, 4: 1, 5: 1, 9: 1}

# expected_times_appearing = [3, 1, 0, 0, 3, 3]
# expected_similarities = [3 * 3, 4, 2 * 0, 1 * 0, 3 * 3, 3 * 3]
expected_similarities = [9, 4, 0, 0, 9, 9]

# expected_total_similarity = 9 + 4 + 0 + 0 + 9 + 9
expected_total_similarity = 31  # sum of similarities


def test_get_similarities():
    similiarities = get_similarities(*example_columns)
    assert expected_similarities == similiarities


def test_get_total_similarities():
    total_similarity = get_total_similarities(example_data)
    assert expected_total_similarity == total_similarity
