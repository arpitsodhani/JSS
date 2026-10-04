# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def chain(seq, ans):
    for i in range(len(seq) - 1):
        ans.append((seq[i][1], seq[i + 1][1]))
    return seq[-1] if seq else None

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2
        a = data[p:p + n]
        p += n
        elves = sorted(((a[i], i + 1) for i in range(n)))
        ans = []
        if m > 0:
            if 2 * m > n:
                out.append('-1')
                continue
            rem = elves[:n - 2 * m]
            victims = elves[n - 2 * m:n - m]
            survivors = elves[n - m:]
            last = chain(rem, ans)
            if last is not None:
                ans.append((last[1], victims[0][1]))
            for i in range(m):
                ans.append((survivors[i][1], victims[i][1]))
            out.append(str(len(ans)))
            out.extend((f'{x} {y}' for x, y in ans))
        else:
            if sum(a) - elves[-1][0] < elves[-1][0]:
                out.append('-1')
                continue
            strongest = elves[-1]
            second = elves[-2]
            h = strongest[0]
            i = 0
            while elves[i][0] < h:
                ans.append((elves[i][1], strongest[1]))
                h -= elves[i][0]
                i += 1
            last = chain(elves[i:n - 2], ans)
            if last is not None:
                ans.append((last[1], second[1]))
            ans.append((second[1], strongest[1]))
            out.append(str(len(ans)))
            out.extend((f'{x} {y}' for x, y in ans))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
