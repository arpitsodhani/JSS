# CLAUSE: setup_environment
import sys
from collections import defaultdict

MOD = 998244353

# CLAUSE: solve_logic
def add_item(dp, value):
    updated = defaultdict(int)
    for total, ways in dp.items():
        updated[total] = (updated[total] + ways) % MOD

        if value == 0:
            updated[total] = (updated[total] + ways) % MOD
        elif total == value:
            updated[total + value] = (updated[total + value] + ways) % MOD
        elif total == value * 3:
            updated[total] = (updated[total] + ways) % MOD

    return updated

def solve_case(arr):
    dp = {0: 1}
    for value in arr:
        dp = add_item(dp, value)
    return sum(dp.values()) % MOD

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    it = iter(tokens)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
        out.append(str(solve_case(arr)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
