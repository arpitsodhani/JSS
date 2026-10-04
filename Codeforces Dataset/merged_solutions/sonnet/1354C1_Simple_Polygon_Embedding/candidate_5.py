# CLAUSE: setup_environment
import sys
from math import atan, tan

# CLAUSE: solve_logic
def build_outputs(numbers):
    pi_value = 4.0 * atan(1.0)
    output_lines = []
    index = 1
    total = numbers[0]
    while index <= total:
        n = numbers[index]
        value = 1.0 / tan(pi_value / (2.0 * n))
        output_lines.append(format(value, ".9f"))
        index += 1
    return output_lines

# CLAUSE: finish_program
items = [int(x) for x in sys.stdin.buffer.read().split()]
sys.stdout.write("\n".join(build_outputs(items)))
