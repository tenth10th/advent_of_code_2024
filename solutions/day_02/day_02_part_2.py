from day_02_part_1 import (
    get_safe_report_count,
    parse_reports,
    check_report_safety,
    Report,
)
import logging
import sys

log = logging.getLogger("day_02")


def check_dampened_report_safety(report: Report) -> bool:
    """
    Determine the safety of a Report, before and after "problem-dampening"
    (omitting a single measurement)
    """
    # If the Report is already safe, no further work required...
    if check_report_safety(report):
        return True

    for i in range(len(report)):
        # "Dampen" a copy of the report by removing one measurement
        report_copy = list(report)
        report_copy.pop(i)
        if check_report_safety(report_copy):
            log.debug(describe_dampening(report_copy, i))
            return True

    return False


def describe_dampening(report: Report, i: int) -> str:
    """
    Describe a problem-dampened Report, given an offset into the list of integers
    (assumes an element formerly at [i] has already been removed...)
    """
    fixed_report = list(report)
    # Insert * to represent the single removed element
    fixed_report.insert(i, "*")
    # Represent the list as a string
    fixed_report_str = repr(fixed_report)
    # Remove single-quotes for a better look
    fixed_report_str = fixed_report_str.replace("'", "")
    return f"   (with [{i}] removed: {fixed_report_str})"


if __name__ == "__main__":

    log_level = logging.INFO
    if "-d" in sys.argv:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level)

    with open("puzzle_input.txt", "r") as f:
        text_data = f.read()

    reports = parse_reports(text_data)
    safe_reports_count = get_safe_report_count(reports, check_dampened_report_safety)

    log.info(f"Safe Reports Found (post-problem-dampening): {safe_reports_count:,}")
