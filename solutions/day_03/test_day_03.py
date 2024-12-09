import pytest

#              1                            2                       3       4  
#           v------v                    v------v                v-------vv------v
example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

expected_muls = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

expected_results = [8, 25, 88, 40]

expected_sum = 161

def test_something():
    assert 1 == 1
