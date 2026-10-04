# CLAUSE: setup_environment
import sys
from collections import deque
from array import array

STEPS = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    x1, y1, x2, y2 = data[2] - 1, data[3] - 1, data[4] - 1, data[5] - 1
    ptr = 6
    total = n * m

    def cell(r, c):
        return r * m + c

    def coords(v):
        return divmod(v, m)

    moves = [[] for _ in range(total)]
    attack = [bytearray(total) for _ in range(total)]

    for r in range(n):
        row_base = r * m
        for c in range(m):
            v = row_base + c
            cur = moves[v]
            for dr, dc in STEPS:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    u = nr * m + nc
                    cur.append(u)
                    attack[v][u] = 1

    white_target = cell(n // 2 - 1, m // 2 - 1)
    black_target = cell(n // 2, m // 2 - 1)
    count = total * total * 2
    win = bytearray(count)
    left = bytearray(count)
    best = array("i", [-1]) * count
    q = deque()

    def sid(w, b, t):
        return ((w * total + b) << 1) | t

    def unpack(s):
        t = s & 1
        v = s >> 1
        return v // total, v % total, t

    def done(w, b, t):
        if w == b:
            return 2 if t == 0 else 1
        ws = w == white_target and not attack[b][w]
        bs = b == black_target and not attack[w][b]
        if ws and bs:
            return 2 if t == 0 else 1
        if ws:
            return 1
        if bs:
            return 2
        return 0

    for w in range(total):
        wm = len(moves[w])
        for b in range(total):
            base = (w * total + b) << 1
            left[base] = wm
            left[base | 1] = len(moves[b])
            a = done(w, b, 0)
            if a:
                win[base] = a
                q.append(base)
            elif left[base] == 0:
                win[base] = 2
                q.append(base)
            a = done(w, b, 1)
            if a:
                win[base | 1] = a
                q.append(base | 1)
            elif left[base | 1] == 0:
                win[base | 1] = 1
                q.append(base | 1)

    while q:
        s = q.popleft()
        w, b, t = unpack(s)
        cur = win[s]
        pt = t ^ 1
        want = pt + 1
        if pt == 0:
            for old in moves[w]:
                p = sid(old, b, 0)
                if win[p]:
                    continue
                if cur == want:
                    win[p] = want
                    best[p] = w
                    q.append(p)
                else:
                    left[p] -= 1
                    if left[p] == 0:
                        win[p] = cur
                        q.append(p)
        else:
            for old in moves[b]:
                p = sid(w, old, 1)
                if win[p]:
                    continue
                if cur == want:
                    win[p] = want
                    best[p] = b
                    q.append(p)
                else:
                    left[p] -= 1
                    if left[p] == 0:
                        win[p] = cur
                        q.append(p)

    w = cell(x1, y1)
    b = cell(x2, y2)
    turn = 0
    alice = 0 if win[sid(w, b, turn)] == 1 else 1
    out = ["WHITE" if alice == 0 else "BLACK"]

    def play():
        nonlocal w, b, turn
        to = best[sid(w, b, turn)]
        if to < 0:
            return False
        r, c = coords(to)
        out.append(str(r + 1) + " " + str(c + 1))
        if turn == 0:
            w = to
        else:
            b = to
        turn ^= 1
        return True

    if turn == alice:
        if not play() or done(w, b, turn):
            sys.stdout.write("\n".join(out))
            return

    while ptr + 1 < len(data):
        r = data[ptr] - 1
        c = data[ptr + 1] - 1
        ptr += 2
        if r < 0 or c < 0:
            break
        if turn == 0:
            w = cell(r, c)
        else:
            b = cell(r, c)
        turn ^= 1
        if done(w, b, turn):
            break
        if turn == alice:
            if not play() or done(w, b, turn):
                break

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
