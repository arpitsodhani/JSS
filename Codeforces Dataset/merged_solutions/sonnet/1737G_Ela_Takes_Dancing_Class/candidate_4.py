# CLAUSE: setup_environment
import sys

def simulate(n, m, a, s, d):
    p = a[:]
    used = [False] * n

# CLAUSE: solve_logic
    step = 0
    while step < m:
        best = -1
        best_value = 10 ** 100

        i = 0
        while i < n:
            if s[i] == "1" and not used[i] and p[i] < best_value:
                best_value = p[i]
                best = i
            i += 1

        if best == -1:
            break

        boundary = 10 ** 100
        j = 0
        while j < n:
            if j != best and p[best] < p[j] < boundary:
                boundary = p[j]
            j += 1

        nxt = p[best] + d
        if nxt >= boundary:
            nxt = boundary - 1
        p[best] = nxt
        used[best] = True
        step += 1

    return p

def main():
    raw = sys.stdin.buffer.read().split()
    it = iter(raw)
    n = int(next(it))
    m = int(next(it))
    q = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    s = next(it).decode()
    lines = []

    for _ in range(q):
        d = int(next(it))
        idx = int(next(it)) - 1
        final_positions = simulate(n, m, arr, s, d)
        lines.append(str(final_positions[idx]))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
