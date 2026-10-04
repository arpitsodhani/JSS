# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def possible(cnt, last, rem):
    a, b, c, d = cnt

    if a > b + 1 or d > c + 1:
        return False
    if a == b + 1 and c + d > 0:
        return False
    if d == c + 1 and a + b > 0:
        return False

    starts = []
    if last == -1:
        starts = [0, 1, 2, 3]
    else:
        for x in (last - 1, last + 1):
            if 0 <= x <= 3:
                starts.append(x)

    for x in starts:
        if cnt[x] <= 0:
            continue
        nxt = list(cnt)
        nxt[x] -= 1
        if rem == 1:
            return True
        if possible_light(tuple(nxt), x):
            return True
    return False

def possible_light(cnt, last):
    a, b, c, d = cnt

    if a > b + 1 or d > c + 1:
        return False
    if a == b + 1 and c + d > 0:
        return False
    if d == c + 1 and a + b > 0:
        return False

    if last == 0:
        return b > 0
    if last == 3:
        return c > 0
    if last == 1:
        return a > 0 or c > 0
    return b > 0 or d > 0

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    cnt = list(map(int, data[:4]))
    n = sum(cnt)
    ans = []
    last = -1

    for _ in range(n):
        chosen = -1
        cand = [0, 1, 2, 3] if last == -1 else [last - 1, last + 1]

        for x in cand:
            if not (0 <= x <= 3) or cnt[x] == 0:
                continue
            cnt[x] -= 1
            if len(ans) + 1 == n or possible_light(tuple(cnt), x):
                chosen = x
                break
            cnt[x] += 1

        if chosen == -1:
            print("NO")
            return

        ans.append(chosen)
        last = chosen

    print("YES")
    print(*ans)

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
