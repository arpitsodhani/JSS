# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    MOVES = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

    n, m = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    p = n * m

    def idx(x, y):
        return (x - 1) * m + (y - 1)

    def pos(v):
        return v // m + 1, v % m + 1

    neigh = [[] for _ in range(p)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            v = idx(i, j)
            for dx, dy in MOVES:
                ni, nj = i + dx, j + dy
                if 1 <= ni <= n and 1 <= nj <= m:
                    neigh[v].append(idx(ni, nj))

    wt = idx(n // 2, m // 2)
    bt = idx(n // 2 + 1, m // 2)
    w0 = idx(x1, y1)
    b0 = idx(x2, y2)

    atk_wt = bytearray(p)
    atk_bt = bytearray(p)
    for v in range(p):
        for u in neigh[v]:
            if u == wt:
                atk_wt[v] = 1
            if u == bt:
                atk_bt[v] = 1

    def sid(w, b, t):
        return (t * p + w) * p + b

    def terminal(w, b):
        if w == b:
            return -1
        if w == wt and not atk_wt[b]:
            return 0
        if b == bt and not atk_bt[w]:
            return 1
        return -1

    def move_winner(w, b, t, to):
        if t == 0:
            if to == b:
                return 0
            nw, nb = to, b
        else:
            if to == w:
                return 1
            nw, nb = w, to
        if nw == wt and not atk_wt[nb]:
            return 0
        if nb == bt and not atk_bt[nw]:
            return 1
        return -1

    def solve(alice):
        total = 2 * p * p
        win = bytearray(total)
        deg = bytearray(total)
        q = deque()

        for w in range(p):
            for b in range(p):
                if terminal(w, b) != -1:
                    continue
                for t in (0, 1):
                    s = sid(w, b, t)
                    if t == alice:
                        cur = w if t == 0 else b
                        for to in neigh[cur]:
                            if move_winner(w, b, t, to) == alice:
                                win[s] = 1
                                q.append(s)
                                break
                    else:
                        cur = w if t == 0 else b
                        c = 0
                        for to in neigh[cur]:
                            if move_winner(w, b, t, to) != alice:
                                c += 1
                        deg[s] = c
                        if c == 0:
                            win[s] = 1
                            q.append(s)

        while q:
            s = q.popleft()
            b = s % p
            z = s // p
            w = z % p
            t = z // p
            pt = 1 - t

            if pt == 0:
                for pw in neigh[w]:
                    if terminal(pw, b) != -1:
                        continue
                    ps = sid(pw, b, pt)
                    if win[ps]:
                        continue
                    if pt == alice:
                        win[ps] = 1
                        q.append(ps)
                    else:
                        deg[ps] -= 1
                        if deg[ps] == 0:
                            win[ps] = 1
                            q.append(ps)
            else:
                for pb in neigh[b]:
                    if terminal(w, pb) != -1:
                        continue
                    ps = sid(w, pb, pt)
                    if win[ps]:
                        continue
                    if pt == alice:
                        win[ps] = 1
                        q.append(ps)
                    else:
                        deg[ps] -= 1
                        if deg[ps] == 0:
                            win[ps] = 1
                            q.append(ps)

        return win

    white_win = solve(0)
    if white_win[sid(w0, b0, 0)]:
        alice = 0
        win = white_win
        print("WHITE")
    else:
        alice = 1
        win = solve(1)
        print("BLACK")
    sys.stdout.flush()

    w, b, turn = w0, b0, 0

    def make_move():
        global w, b, turn
        cur = w if alice == 0 else b
        for to in neigh[cur]:
            if move_winner(w, b, alice, to) == alice:
                x, y = pos(to)
                print(x, y)
                sys.stdout.flush()
                sys.exit(0)
        for to in neigh[cur]:
            nw, nb = (to, b) if alice == 0 else (w, to)
            if win[sid(nw, nb, 1 - alice)]:
                x, y = pos(to)
                print(x, y)
                sys.stdout.flush()
                if alice == 0:
                    w = to
                else:
                    b = to
                turn = 1 - alice
                return

    if alice == 0:
        make_move()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        a, c = map(int, line.split())
        if a == -1 and c == -1:
            break
        if alice == 0:
            b = idx(a, c)
        else:
            w = idx(a, c)
        make_move()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
