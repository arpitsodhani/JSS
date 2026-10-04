# CLAUSE: setup_environment
import sys
from collections import deque

def ok(a, b):
    if set(a) <= {'a'} and set(b) <= {'b'}:
        return True
    if set(a) <= {'b'} and set(b) <= {'a'}:
        return True
    return False

def alternating(x):
    return x == "" or "".join(x[i] for i in range(len(x)) if i == 0 or x[i] != x[i - 1]) == x

def transform(a, b, i, j):
    return b[0:j] + a[i:], a[0:i] + b[j:]

def all_next(a, b):
    la = len(a)
    lb = len(b)
    i = 0
    while i <= la:
        j = 0
        while j <= lb:
            if i != 0 or j != 0:
                yield i, j, transform(a, b, i, j)
            j += 1
        i += 1

def build_answer(goal, back, op):
    path = []
    cur = goal
    while back[cur] is not None:
        path.append(op[cur])
        cur = back[cur]
    path.reverse()
    return [str(len(path))] + [str(x) + " " + str(y) for x, y in path]

def run_bfs(start, accept, enqueue):
    waiting = deque([start])
    back = {start: None}
    op = {}
    while waiting:
        a, b = waiting.popleft()
        for i, j, nxt in all_next(a, b):
            if nxt in back:
                continue
            back[nxt] = (a, b)
            op[nxt] = (i, j)
            if accept(nxt):
                return build_answer(nxt, back, op)
            if enqueue(nxt):
                waiting.append(nxt)
    return []

# CLAUSE: solve_logic
def solve():
    items = sys.stdin.read().split()
    if len(items) < 2:
        return

    first, second = items[0], items[1]
    start = (first, second)
    if ok(first, second):
        sys.stdout.write("0")
        return

    total = len(first) + len(second)
    answer = run_bfs(start, lambda p: ok(p[0], p[1]), lambda p: len(p[0]) + len(p[1]) == total and alternating(p[0]) and alternating(p[1]))

    if not answer:
        number_a = first.count('a') + second.count('a')
        number_b = total - number_a
        targets = (('a' * number_a, 'b' * number_b), ('b' * number_b, 'a' * number_a))
        answer = run_bfs(start, lambda p: p == targets[0] or p == targets[1], lambda p: True)

    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
