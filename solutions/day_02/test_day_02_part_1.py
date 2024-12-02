from day_02_part_1 import get_safe_report_count, parse_reports, check_report_safety
import logging

log = logging.getLogger("day_02")
logging.basicConfig(level=logging.DEBUG)


def test_get_safe_report_count():
    safe_report_count = get_safe_report_count(expected_reports, check_report_safety)
    assert safe_report_count == 2


def test_parse_reports():
    reports = parse_reports(example_data)
    assert reports == expected_reports


def test_check_report_safety():
    for report, expected_safety in expected_report_safety:
        safe = check_report_safety(report)
        assert safe == expected_safety


example_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# Raw data parsed as lists of integers
expected_reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

# Tuples of (Report, Safety Boolean)
expected_report_safety = [
    (expected_reports[0], True),
    (expected_reports[1], False),
    (expected_reports[2], False),
    (expected_reports[3], False),
    (expected_reports[4], False),
    (expected_reports[5], True),
]
