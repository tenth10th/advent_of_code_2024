from test_day_02_part_1 import expected_reports
from day_02_part_2 import check_dampened_report_safety, describe_dampening


def test_check_dampened_report_safety():
    for report, expected_safety in expected_dampened_report_safety:
        safety = check_dampened_report_safety(report)
        assert safety == expected_safety


def test_describe_dampening():
    offset = 2
    report = [1, 2, 9, 4, 5]
    report.pop(offset)
    description = describe_dampening(report, offset)
    assert description == "   (with [2] removed: [1, 2, *, 4, 5])"


# Tuples of (Report, Safety Boolean)
expected_dampened_report_safety = [
    (expected_reports[0], True),
    (expected_reports[1], False),
    (expected_reports[2], False),
    (expected_reports[3], True),
    (expected_reports[4], True),
    (expected_reports[5], True),
]
