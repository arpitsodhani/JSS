# Clause setup_environment [Confidence: 0.40]
import sys
from collections import defaultdict

MOD = 1000000007


# Clause solve_logic [Confidence: 0.80]
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    q = nums[0]
    at = 1
    ans = []

    for _ in range(q):
        n, k = nums[at], nums[at + 1]
        at += 2
        arr = nums[at:at + n]
        at += n

        max_blocks = [0] * (n + 1)
        counts = [0] * (n + 1)
        counts[0] = 1
        last_k = {}

        for zero_i in range(n):
            i = zero_i + 1
            color = arr[zero_i]
            max_blocks[i] = max_blocks[i - 1]
            counts[i] = counts[i - 1]

            if color not in last_k:
                last_k[color] = deque()
            dq = last_k[color]
            dq.append(i)
            if len(dq) > k:
                dq.popleft()

            if len(dq) == k:
                before = dq[0] - 1
                candidate = max_blocks[before] + 1
                if candidate > max_blocks[i]:
                    max_blocks[i] = candidate
                    counts[i] = counts[before]
                elif candidate == max_blocks[i]:
                    counts[i] = (counts[i] + counts[before]) % MOD

        ans.append(str(counts[n] % MOD))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


