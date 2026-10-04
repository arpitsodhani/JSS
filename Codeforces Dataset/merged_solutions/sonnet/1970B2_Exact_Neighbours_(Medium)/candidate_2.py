# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    a = [0] + values[1:1 + n]
    pos = [(0, 0) for _ in range(n + 1)]
    ans = [1 for _ in range(n + 1)]
    used = set()
    pos[1] = (1, 1)
    used.add(1)
    for i in range(2, n + 1):
        d = a[i]
        if d == 0:
            sys.stdout.write("NO\n")
            return
        if d + 1 <= n and d + 1 not in used:
            pos[i] = (d + 1, 1)
            ans[i] = 1
            used.add(d + 1)
            continue
        col = 0
        for c in range(1, n + 1):
            if c not in used:
                col = c
                break
        if col == 0:
            sys.stdout.write("NO\n")
            return
        ok = False
        for j in range(1, i):
            x, y = pos[j]
            rest = d - abs(col - x)
            if rest < 0:
                continue
            y1 = y + rest
            y2 = y - rest
            if 1 <= y1 <= n:
                pos[i] = (col, y1)
                ans[i] = j
                ok = True
            elif 1 <= y2 <= n:
                pos[i] = (col, y2)
                ans[i] = j
                ok = True
            if ok:
                break
        if not ok:
            sys.stdout.write("NO\n")
            return
        used.add(col)
    out = ["YES"]
    out.extend(str(pos[i][0]) + " " + str(pos[i][1]) for i in range(1, n + 1))
    out.append(" ".join(map(str, ans[1:])))
    sys.stdout.write("\n".join(out) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
