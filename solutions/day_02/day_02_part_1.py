import logging
import sys

log = logging.getLogger("day_02")

Report = list[int]


def get_safe_report_count(reports: list[Report], check_report_safety) -> int:
    """
    Get the count of Safe reports from a text data file of Reports
    """
    safe_reports_count = 0
    log.debug(f"Found {len(reports):,} reports...")
    for report in reports:
        if check_report_safety(report):
            safe_reports_count += 1

    return safe_reports_count


def parse_reports(text_data: str) -> list[Report]:
    """
    Parse a Text Reports data file into a list of Report objects (list of integers)
    """
    reports = list()
    for line in text_data.split("\n"):
        if not line.strip():
            continue
        report: Report = [int(digit) for digit in line.split(" ")]
        if report:
            reports.append(report)
    log.info(f"Read {len(reports):,} reports from file")
    return reports


def check_report_safety(report: Report) -> bool:
    """
    Return the safety of a Report as a boolean
    (As per the rules: https://adventofcode.com/2024/day/2#part2 )
    """
    last_measurement = None
    increasing = None
    log.debug(f"Report: {report}")
    for i, measurement in enumerate(report):

        if last_measurement is not None:

            # Safe measurements must differ by 1, 2, or 3
            diff = abs(measurement - last_measurement)
            if diff not in (1, 2, 3):
                log.debug(f"   [{i}] diff: {diff} - Not safe!")
                return False

            # Safe measurements must consistently Increase or Decrease
            if measurement > last_measurement:
                if increasing is False:
                    log.debug(
                        f"   [{i}] Was Decreasing, but {measurement} > {last_measurement}"
                    )
                    return False
                increasing = True
            else:
                if increasing is True:
                    log.debug(
                        f"   [{i}] Was Increasing, but {measurement} < {last_measurement}"
                    )
                    return False
                increasing = False

        last_measurement = measurement

    log.debug("   Safe!")
    return True


if __name__ == "__main__":

    log_level = logging.INFO
    if "-d" in sys.argv:
        log_level = logging.DEBUG
        print("(Detailed Output)")
    else:
        print("(High-level Output: Run with -d for verbose debugging)")

    logging.basicConfig(level=log_level, format="%(message)s")

    with open("puzzle_input.txt", "r") as f:
        text_data = f.read()

    reports = parse_reports(text_data)
    safe_reports_count = get_safe_report_count(reports, check_report_safety)

    log.info(f"Safe Reports Found: {safe_reports_count:,}")
