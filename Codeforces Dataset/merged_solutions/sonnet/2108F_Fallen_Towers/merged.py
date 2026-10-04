# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
def can_make(a, want):
    n = len(a)
    expire = [0] * (n + 1)
    falling = 0
    start = n - want
    for i, height in enumerate(a):
        falling -= expire[i]
        need = i - start
        if need < 0:
            need = 0
        if falling < need:
            return False
        end = i + height + falling - need + 1
        falling += 1
        if end < n:
            expire[end] += 1
    return True

def answer_case(a):
    lo, hi = 1, len(a) + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if can_make(a, mid):
            lo = mid
        else:
            hi = mid
    return lo

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n
        out.append(str(answer_case(a)))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


