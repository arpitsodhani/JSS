# CLAUSE: setup_environment
import sys
from collections import deque

DELTAS = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return

    n, m = nums[0], nums[1]
    total = n * m
    start_w = (nums[2] - 1) * m + nums[3] - 1
    start_b = (nums[4] - 1) * m + nums[5] - 1
    index = 6

    moves = []
    masks = [0] * total
    for p in range(total):
        r, c = divmod(p, m)
        cur = []
        mask = 0
        for dr, dc in DELTAS:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m:
                q = nr * m + nc
                cur.append(q)
                mask |= 1 << q
        moves.append(tuple(cur))
        masks[p] = mask

    white_goal = (n // 2 - 1) * m + (m // 2 - 1)
    black_goal = (n // 2) * m + (m // 2 - 1)
    size = total * total * 2
    winner = [0] * size
    remain = [0] * size
    choice = [-1] * size
    que = deque()

    def make_id(w, b, t):
        return ((w * total + b) * 2) + t

    def split_id(s):
        t = s % 2
        x = s // 2
        return x // total, x % total, t

    def result(w, b, t):
        if w == b:
            return 2 if t == 0 else 1
        white_ok = w == white_goal and ((masks[b] >> w) & 1) == 0
        black_ok = b == black_goal and ((masks[w] >> b) & 1) == 0
        if white_ok:
            if black_ok:
                return 2 if t == 0 else 1
            return 1
        if black_ok:
            return 2
        return 0

    for w in range(total):
        for b in range(total):
            s0 = make_id(w, b, 0)
            s1 = s0 + 1
            remain[s0] = len(moves[w])
            remain[s1] = len(moves[b])
            r0 = result(w, b, 0)
            r1 = result(w, b, 1)
            if r0:
                winner[s0] = r0
                que.append(s0)
            elif remain[s0] == 0:
                winner[s0] = 2
                que.append(s0)
            if r1:
                winner[s1] = r1
                que.append(s1)
            elif remain[s1] == 0:
                winner[s1] = 1
                que.append(s1)

    while que:
        s = que.popleft()
        w, b, t = split_id(s)
        cur = winner[s]
        prior = t ^ 1
        owner = prior + 1
        if prior == 0:
            for prev_w in moves[w]:
                p = make_id(prev_w, b, prior)
                if winner[p]:
                    continue
                if cur == owner:
                    winner[p] = owner
                    choice[p] = w
                    que.append(p)
                else:
                    remain[p] -= 1
                    if remain[p] == 0:
                        winner[p] = cur
                        que.append(p)
        else:
            for prev_b in moves[b]:
                p = make_id(w, prev_b, prior)
                if winner[p]:
                    continue
                if cur == owner:
                    winner[p] = owner
                    choice[p] = b
                    que.append(p)
                else:
                    remain[p] -= 1
                    if remain[p] == 0:
                        winner[p] = cur
                        que.append(p)

    w = start_w
    b = start_b
    turn = 0
    alice = 0 if winner[make_id(w, b, turn)] == 1 else 1
    ans = ["WHITE" if alice == 0 else "BLACK"]

    while True:
        if turn == alice:
            to = choice[make_id(w, b, turn)]
            if to == -1:
                break
            rr, cc = divmod(to, m)
            ans.append(f"{rr + 1} {cc + 1}")
            if turn == 0:
                w = to
            else:
                b = to
            turn ^= 1
            if result(w, b, turn):
                break
        if index + 1 >= len(nums):
            break
        rr = nums[index] - 1
        cc = nums[index + 1] - 1
        index += 2
        if rr < 0 or cc < 0:
            break
        if turn == 0:
            w = rr * m + cc
        else:
            b = rr * m + cc
        turn ^= 1
        if result(w, b, turn):
            break

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
