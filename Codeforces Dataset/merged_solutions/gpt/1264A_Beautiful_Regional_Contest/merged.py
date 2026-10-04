# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, p):
    limit = n // 2
    groups = []
    i = 0
    while i < n:
        j = i
        while j < n and p[j] == p[i]:
            j += 1
        groups.append(j - i)
        i = j

    if len(groups) < 3:
        return (0, 0, 0)

    g = groups[0]
    if g >= limit:
        return (0, 0, 0)

    s = 0
    idx = 1
    while idx < len(groups) and s <= g:
        s += groups[idx]
        idx += 1

    b = 0
    while idx < len(groups) and g + s + b + groups[idx] <= limit:
        b += groups[idx]
        idx += 1

    if g > 0 and s > g and b > g and g + s + b <= limit:
        return (g, s, b)
    return (0, 0, 0)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        p = data[pos:pos + n]
        pos += n
        out.append("%d %d %d" % solve_case(n, p))
    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
