# CLAUSE: setup_environment
import sys
import math
from functools import reduce
from operator import xor

# CLAUSE: solve_logic
def pair_result(values):
    small, large = sorted(values)
    diff = large - small
    if diff == 0:
        return small == 0
    target = (diff + math.isqrt(diff * diff * 5)) // 2
    return small == target

def decide(count, values):
    if count == 1:
        return values[0] != 0
    if count == 2:
        return not pair_result(values)
    return reduce(xor, values, 0) != 0

# CLAUSE: finish_program
tokens = sys.stdin.buffer.read().split()
if tokens:
    total = int(tokens[0])
    numbers = [int(x) for x in tokens[1:1 + total]]
    sys.stdout.write("BitLGM" if decide(total, numbers) else "BitAryo")
