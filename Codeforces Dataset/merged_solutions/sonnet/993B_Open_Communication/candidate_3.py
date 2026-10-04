# CLAUSE: setup_environment
import sys

def mask_pair(a, b):
    return (1 << a) | (1 << b)

def one_bit_number(mask):
    return mask.bit_length() - 1

# CLAUSE: solve_logic
def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    n = data[0]
    m = data[1]
    k = 2

    first = []
    while len(first) < n:
        first.append(mask_pair(data[k], data[k + 1]))
        k += 2

    second = []
    while len(second) < m:
        second.append(mask_pair(data[k], data[k + 1]))
        k += 2

    answer_bits = 0
    for x in first:
        for y in second:
            common = x & y
            if common.bit_count() == 1:
                answer_bits |= common

    if answer_bits.bit_count() == 1:
        print(one_bit_number(answer_bits))
        return

    for x in first:
        seen = 0
        for y in second:
            common = x & y
            if common.bit_count() == 1:
                seen |= common
        if seen.bit_count() > 1:
            print(-1)
            return

    for y in second:
        seen = 0
        for x in first:
            common = x & y
            if common.bit_count() == 1:
                seen |= common
        if seen.bit_count() > 1:
            print(-1)
            return

    print(0)

# CLAUSE: finish_program
main()
