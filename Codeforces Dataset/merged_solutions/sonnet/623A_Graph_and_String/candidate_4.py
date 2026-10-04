# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    m = int(tokens[1])
    rows = [0] * n
    p = 2
    for _ in range(m):
        u = int(tokens[p]) - 1
        v = int(tokens[p + 1]) - 1
        p += 2
        rows[u] |= 1 << v
        rows[v] |= 1 << u

    full = (1 << n) - 1
    for i in range(n):
        rows[i] |= 1 << i

    side = [-1] * n
    stack = []
    for start in range(n):
        if side[start] != -1:
            continue
        side[start] = 0
        stack.append(start)
        while stack:
            v = stack.pop()
            missing = full ^ rows[v]
            while missing:
                bit = missing & -missing
                u = bit.bit_length() - 1
                missing -= bit
                if side[u] == -1:
                    side[u] = side[v] ^ 1
                    stack.append(u)
                elif side[u] == side[v]:
                    sys.stdout.write("No\n")
                    return

    ans = []
    for i in range(n):
        if rows[i] == full:
            ans.append("b")
        elif side[i] == 0:
            ans.append("a")
        else:
            ans.append("c")

    for i in range(n):
        for j in range(i + 1, n):
            pair_ok = not ((ans[i] == "a" and ans[j] == "c") or (ans[i] == "c" and ans[j] == "a"))
            if bool(rows[i] & (1 << j)) != pair_ok:
                sys.stdout.write("No\n")
                return

    sys.stdout.write("Yes\n" + "".join(ans) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
