# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def solve_one(n, a):
    if sum(a) != n:
        return 0

    total = 0
    stack = [(1, tuple(a), ())]

    while stack:
        k, rem, picked = stack.pop()
        if k <= n:
            for r in range(k, 0, -1):
                if rem[r - 1] > 0:
                    nxt = list(rem)
                    nxt[r - 1] -= 1
                    stack.append((k + 1, tuple(nxt), picked + (r,)))
            continue

        ways_stack = [(1, 0)]
        ways = 0
        while ways_stack:
            idx, mask = ways_stack.pop()
            if idx > n:
                ways += 1
                continue
            r = picked[idx - 1]
            if r < idx:
                q = max(r, n + 1 - idx)
                bit = 1 << (q - 1)
                if mask & bit == 0:
                    ways_stack.append((idx + 1, mask | bit))
            else:
                for c in range(1, idx + 1):
                    q = max(idx, n + 1 - c)
                    bit = 1 << (q - 1)
                    if mask & bit == 0:
                        ways_stack.append((idx + 1, mask | bit))
        total = (total + ways) % MOD

    return total

# CLAUSE: finish_program
def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    t = nums[0]
    at = 1
    answers = []
    for _ in range(t):
        n = nums[at]
        at += 1
        a = nums[at:at + n]
        at += n
        answers.append(str(solve_one(n, a)))
    print("\n".join(answers))

main()
