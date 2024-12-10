import logging
import sys

from day_03_part_1 import (
    parse_muls,
    parse_numbers,
    multiply_results,
    mul_chars,
    allowed_chars,
)

log = logging.getLogger("day_03")

do_chars = list("do()")
dont_chars = list("don't()")

def get_result_sum(text_data):
    enabled_muls, disabled_muls, invalid_muls = parse_muls(text_data)
    print(f"Found {len(enabled_muls):,} Enabled, {len(disabled_muls):,} Disabled, {len(invalid_muls):,} Invalid")
    number_groups = [parse_numbers(mul) for mul in enabled_muls]
    total_numbers = sum([len(group) for group in number_groups])
    log.info(f"Found {len(number_groups)} groups of {total_numbers} total numbers")
    log.info(f"    (An average of {total_numbers / len(number_groups)} numbers per group)")
    results = multiply_results(number_groups)
    log.info(f"Found {len(results)} multiplication results")
    answer = sum(results)
    log.info(f"Answer: {answer:,} -> {answer}")
    return answer

def parse_muls(text_data: str) -> tuple[list[str], list[str], list[str]]:
    in_mul = True
    enabled = True
    previous = list()
    this_mul = list()
    enabled_muls = list()
    disabled_muls = list()
    invalid_muls = list()
    # iterate through characters in text, with indexes
    for i, c in enumerate(text_data):
        if in_mul:
            if c in allowed_chars:
                this_mul.append(c)
            if c not in allowed_chars or c == ")":
                in_mul = False
                this_mul_str = "".join(this_mul).strip()
                if this_mul_str and ")" in this_mul:
                    if enabled:
                        enabled_muls.append(this_mul_str)
                    else:
                        disabled_muls.append(this_mul_str)
                elif this_mul_str:
                    invalid_muls.append(this_mul_str)
                this_mul = list()

        # accumulate a list of the characters we've seen so far
        previous.append(c)

        if previous[-4:] == mul_chars:
            # we seem to be "in" a mul right now!
            in_mul = True
            this_mul.extend(mul_chars)

        if previous[-4:] == do_chars:
            # do() enables muls
            enabled = True

        if previous[-7:] == dont_chars:
            # don't() disables muls
            enabled = False

    return enabled_muls, disabled_muls, invalid_muls

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

    get_result_sum(text_data)