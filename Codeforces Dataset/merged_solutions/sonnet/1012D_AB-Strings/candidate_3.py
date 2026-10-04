# CLAUSE: setup_environment
import sys

def mono_pair(a, b):
    return (all(x == 'a' for x in a) and all(x == 'b' for x in b)) or (all(x == 'b' for x in a) and all(x == 'a' for x in b))

def no_equal_neighbors(x):
    return all(x[k] != x[k - 1] for k in range(1, len(x)))

def make_move(pair, cut_a, cut_b):
    a, b = pair
    return b[:cut_b] + a[cut_a:], a[:cut_a] + b[cut_b:]

def search(start, accept, filtered, total):
    queue = [start]
    head = 0
    previous = {start: None}
    chosen = {}
    while head < len(queue):
        state = queue[head]
        head += 1
        a, b = state
        for cut_a in range(len(a) + 1):
            for cut_b in range(len(b) + 1):
                if cut_a == 0 and cut_b == 0:
                    continue
                nxt = make_move(state, cut_a, cut_b)
                if nxt in previous:
                    continue
                previous[nxt] = state
                chosen[nxt] = (cut_a, cut_b)
                if accept(nxt):
                    route = []
                    cur = nxt
                    while previous[cur] is not None:
                        route.append(chosen[cur])
                        cur = previous[cur]
                    route.reverse()
                    return route
                if not filtered or (len(nxt[0]) + len(nxt[1]) == total and no_equal_neighbors(nxt[0]) and no_equal_neighbors(nxt[1])):
                    queue.append(nxt)
    return None

# CLAUSE: solve_logic
def solve():
    words = sys.stdin.read().split()
    if len(words) < 2:
        return

    s, t = words[0], words[1]
    if mono_pair(s, t):
        print(0)
        return

    total = len(s) + len(t)
    start = (s, t)

    ans = search(start, lambda p: mono_pair(p[0], p[1]), True, total)

    if ans is None:
        a_total = s.count('a') + t.count('a')
        b_total = total - a_total
        want_a = ('a' * a_total, 'b' * b_total)
        want_b = ('b' * b_total, 'a' * a_total)
        ans = search(start, lambda p: p == want_a or p == want_b, False, total)

    lines = [str(len(ans))]
    for cut_a, cut_b in ans:
        lines.append(str(cut_a) + " " + str(cut_b))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
