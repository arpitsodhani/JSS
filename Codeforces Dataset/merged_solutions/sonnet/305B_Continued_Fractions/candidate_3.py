# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def advance_fraction(numerator, denominator, expected, last):
    if denominator == 0:
        return None

    part, rest = divmod(numerator, denominator)
    if part != expected:
        return None

    if last:
        return (0, 1) if rest == 0 else None

    if rest == 0:
        return None

    return denominator, rest


def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    numerator = nums[0]
    denominator = nums[1]
    count = nums[2]
    answer = "YES"

    for pos, expected in enumerate(nums[3:3 + count]):
        state = advance_fraction(numerator, denominator, expected, pos + 1 == count)
        if state is None:
            answer = "NO"
            break
        numerator, denominator = state

    sys.stdout.write(answer)

# CLAUSE: finish_program
main()
