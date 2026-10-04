# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        a = data[pos:pos + n]
        pos += n
        special = data[pos:pos + k]
        pos += k
        special.sort()

        x = a[special[0] - 1]
        counts = [0] * (k + 1)
        prev = 0
        changes = 0

        for i in range(1, n + 2):
            cur = 0 if i == n + 1 else (a[i - 1] ^ x)
            if cur != prev:
                bucket = bisect_left(special, i)
                counts[bucket] += 1
                changes += 1
            prev = cur

        out.append(str(max(changes // 2, max(counts))))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
