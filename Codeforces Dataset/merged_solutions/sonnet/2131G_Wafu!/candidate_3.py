# CLAUSE: setup_environment
import sys
from bisect import bisect_left, insort

MOD = 1000000007

# CLAUSE: solve_logic
def run_case(k, values):
    ordered = sorted(values)
    present = set(values)
    result = 1
    while k and ordered:
        m = ordered.pop(0)
        if m not in present:
            continue
        present.remove(m)
        result = result * m % MOD
        for v in range(1, m):
            if v not in present:
                present.add(v)
                insort(ordered, v)
        k -= 1
    return result

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    tests = nums[0]
    at = 1
    out = []
    for _ in range(tests):
        n, k = nums[at], nums[at + 1]
        at += 2
        out.append(str(run_case(k, nums[at:at + n])))
        at += n
    print("\n".join(out))

# CLAUSE: finish_program
main()
