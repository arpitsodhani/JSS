# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def compress(a):
    vals = sorted(set(a))
    return vals, [bisect_left(vals, x) for x in a]

def case_result(a):
    vals, ids = compress(a)
    freq = [0] * len(vals)
    for x in ids:
        freq[x] += 1

    base = [0] * len(vals)
    s = 0
    for i, c in enumerate(freq):
        base[i] = s
        s += c

    used = [0] * len(vals)
    positions = [0] * len(a)
    for original_pos, x in enumerate(ids):
        rank = base[x] + used[x]
        used[x] += 1
        positions[rank] = original_pos

    best = 0
    streak = 0
    prev = -1
    for p in positions:
        if p > prev:
            streak += 1
        else:
            streak = 1
        if streak > best:
            best = streak
        prev = p
    return len(a) - best

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    k = 1
    ans = []
    for _ in range(q):
        n = int(data[k])
        k += 1
        a = [int(data[k + i]) for i in range(n)]
        k += n
        ans.append(str(case_result(a)))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
