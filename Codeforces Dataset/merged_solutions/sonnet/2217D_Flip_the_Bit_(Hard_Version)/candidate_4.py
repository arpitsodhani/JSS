# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def solve_case(a, special):
    special.sort()
    base = a[special[0] - 1]
    k = len(special)
    buckets = [0] * (k + 1)
    active = False
    segments = 0

# CLAUSE: solve_logic
    for idx, value in enumerate(a, 1):
        bad = value != base
        if bad and not active:
            segments += 1
            buckets[bisect_left(special, idx)] += 1
        elif active and not bad:
            buckets[bisect_left(special, idx)] += 1
        active = bad

    if active:
        buckets[k] += 1

    largest = max(buckets)
    return segments if segments > largest else largest

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    ans = []

    for _ in range(t):
        n = data[ptr]
        k = data[ptr + 1]
        ptr += 2
        a = data[ptr:ptr + n]
        ptr += n
        special = data[ptr:ptr + k]
        ptr += k
        ans.append(str(solve_case(a, special)))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
