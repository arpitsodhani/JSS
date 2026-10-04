# CLAUSE: setup_environment
import sys
from collections import deque
from array import array

JUMPS = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    m = data[1]
    total = n * m

    def inside(r, c):
        return 0 <= r < n and 0 <= c < m

    def pack(r, c):
        return r * m + c

    nexts = [None] * total
    attacks = [set() for _ in range(total)]
    for r in range(n):
        for c in range(m):
            p = pack(r, c)
            arr = []
            for dr, dc in JUMPS:
                nr = r + dr
                nc = c + dc
                if inside(nr, nc):
                    q = pack(nr, nc)
                    arr.append(q)
                    attacks[p].add(q)
            nexts[p] = arr

    wg = pack(n // 2 - 1, m // 2 - 1)
    bg = pack(n // 2, m // 2 - 1)
    states = total * total * 2
    owner = bytearray(states)
    deg = bytearray(states)
    reply = array("i", [-1]) * states
    dq = deque()

    def state(w, b, side):
        return ((w * total + b) << 1) + side

    def parts(s):
        side = s & 1
        s >>= 1
        return s // total, s % total, side

    def final_owner(w, b, side):
        if w == b:
            return 2 if side == 0 else 1
        white = w == wg and w not in attacks[b]
        black = b == bg and b not in attacks[w]
        if white and black:
            return 2 if side == 0 else 1
        if white:
            return 1
        if black:
            return 2
        return 0

    for w in range(total):
        a = len(nexts[w])
        for b in range(total):
            s = state(w, b, 0)
            deg[s] = a
            deg[s + 1] = len(nexts[b])
            for side in (0, 1):
                t = s + side
                got = final_owner(w, b, side)
                if got:
                    owner[t] = got
                    dq.append(t)
                elif deg[t] == 0:
                    owner[t] = 3 - (side + 1)
                    dq.append(t)

    while dq:
        cur_state = dq.popleft()
        w, b, side = parts(cur_state)
        won_by = owner[cur_state]
        prev_side = side ^ 1
        prev_owner = prev_side + 1
        if prev_side == 0:
            sources = nexts[w]
            for old_w in sources:
                ps = state(old_w, b, 0)
                if owner[ps]:
                    continue
                if won_by == prev_owner:
                    owner[ps] = prev_owner
                    reply[ps] = w
                    dq.append(ps)
                else:
                    deg[ps] -= 1
                    if deg[ps] == 0:
                        owner[ps] = won_by
                        dq.append(ps)
        else:
            sources = nexts[b]
            for old_b in sources:
                ps = state(w, old_b, 1)
                if owner[ps]:
                    continue
                if won_by == prev_owner:
                    owner[ps] = prev_owner
                    reply[ps] = b
                    dq.append(ps)
                else:
                    deg[ps] -= 1
                    if deg[ps] == 0:
                        owner[ps] = won_by
                        dq.append(ps)

    w = pack(data[2] - 1, data[3] - 1)
    b = pack(data[4] - 1, data[5] - 1)
    side = 0
    alice = 0 if owner[state(w, b, side)] == 1 else 1
    out = ["WHITE" if alice == 0 else "BLACK"]

    def emit_move():
        nonlocal w, b, side
        move_to = reply[state(w, b, side)]
        if move_to == -1:
            return False
        r, c = divmod(move_to, m)
        out.append(f"{r + 1} {c + 1}")
        if side == 0:
            w = move_to
        else:
            b = move_to
        side ^= 1
        return True

    if side == alice:
        if not emit_move() or final_owner(w, b, side):
            print("\n".join(out))
            return

    i = 6
    while i + 1 < len(data):
        r = data[i] - 1
        c = data[i + 1] - 1
        i += 2
        if r < 0 or c < 0:
            break
        if side == 0:
            w = pack(r, c)
        else:
            b = pack(r, c)
        side ^= 1
        if final_owner(w, b, side):
            break
        if side == alice:
            if not emit_move() or final_owner(w, b, side):
                break

    print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
