import pytest
from day_03_part_2 import parse_muls, get_result_sum

example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

example_enabled = ["mul(2,4)", "mul(8,5)"]

example_number_groups = [[2, 4], [8, 5]]

example_results = [8, 40]

example_answer = 48

def test_get_result_sum():
    answer = get_result_sum(example)
    assert answer == example_answer

def test_parse_muls():
    enabled_muls, disabled_muls, invalid_muls = parse_muls(example)
    assert enabled_muls == example_enabled
