# CLAUSE: setup_environment
import sys
from collections import defaultdict

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tests = values[ptr]
    ptr += 1
    out = []

    for _ in range(tests):
        n = values[ptr]
        k = values[ptr + 1]
        ptr += 2
        colors = values[ptr:ptr + n]
        ptr += n

        best = [0] * (n + 1)
        ways = [0] * (n + 1)
        ways[0] = 1
        seen = defaultdict(list)

        for i, color in enumerate(colors, 1):
            best[i] = best[i - 1]
            ways[i] = ways[i - 1]
            seen[color].append(i)
            bucket = seen[color]
            if len(bucket) >= k:
                start = bucket[-k]
                score = best[start - 1] + 1
                if score > best[i]:
                    best[i] = score
                    ways[i] = ways[start - 1]
                elif score == best[i]:
                    ways[i] = (ways[i] + ways[start - 1]) % MOD

        out.append(str(ways[n] % MOD))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
