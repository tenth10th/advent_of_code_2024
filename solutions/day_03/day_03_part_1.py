import functools
import logging
import operator
import sys

log = logging.getLogger("day_03")


def get_sum_of_mults(text_data: str) -> int:
    valid_muls, invalid_muls = parse_muls(text_data)
    log.info(f"Found {len(valid_muls)} valid muls, {len(invalid_muls)} invalid muls")
    number_groups = [parse_numbers(mul) for mul in valid_muls]
    total_numbers = sum([len(group) for group in number_groups])
    log.info(f"Found {len(number_groups)} groups of {total_numbers} total numbers")
    log.info(f"    (An average of {total_numbers / len(number_groups)} numbers per group)")
    results = multiply_results(number_groups)
    log.info(f"Found {len(results)} multiplication results")
    answer = sum(results)
    log.info(f"Sum of Multiplication Results: {answer:,} => {answer}")
    return answer


mul_chars = list("mul(")
allowed_chars = "0123456789,)"


def parse_muls(text_data: str) -> tuple[list[str], list[str]]:
    in_mult = True
    last_four = list()
    this_mult = list()
    valid_mults = list()
    invalid_mults = list()
    # iterate through characters in text, with indexes
    for i, c in enumerate(text_data):
        if in_mult:
            if c in allowed_chars:
                this_mult.append(c)
            if c not in allowed_chars or c == ")":
                in_mult = False
                this_mult_str = "".join(this_mult).strip()
                if this_mult_str and ")" in this_mult:
                    valid_mults.append(this_mult_str)
                elif this_mult_str:
                    invalid_mults.append(this_mult_str)
                this_mult = list()

        # accumulate a list of the characters we've seen so far
        last_four.append(c)

        if len(last_four) > 4:
            # Limit to last four characters
            last_four = last_four[-4:]

        if last_four == mul_chars:
            # we seem to be "in" a mult right now!
            in_mult = True
            this_mult.extend(last_four)

    return valid_mults, invalid_mults


def parse_numbers(mul):
    numbers_str = mul[4:-1]
    numbers = [int(ns) for ns in numbers_str.split(",")]
    return numbers


def multiply_results(number_groups):
    results = [functools.reduce(operator.mul, group) for group in number_groups]
    return results


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

    get_sum_of_mults(text_data)
