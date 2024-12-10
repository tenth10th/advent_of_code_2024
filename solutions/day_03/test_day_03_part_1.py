from day_03_part_1 import get_sum_of_mults, parse_muls, parse_numbers, multiply_results
import pytest

#              1                            2                       3       4
#           v------v                    v------v                v-------vv------v
example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

expected_muls = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

expected_numbers = [[2, 4], [5, 5], [11, 8], [8, 5]]

expected_results = [8, 25, 88, 40]

expected_sum = 161


def test_get_sum_of_mults():
    result = get_sum_of_mults(example)
    assert result == expected_sum


def test_parse_muls():
    valid_muls, invalid_muls = parse_muls(example)
    assert valid_muls == expected_muls


def test_parse_numbers():
    for i, mul in enumerate(expected_muls):
        numbers = parse_numbers(mul)
        assert numbers == expected_numbers[i]


def test_get_results():
    results = multiply_results(expected_numbers)
    assert results == expected_results
