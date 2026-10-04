# Clause setup_environment [Confidence: 0.60]
import sys
from collections import deque

def one_color(x, c):
    for ch in x:
        if ch != c:
            return False
    return True

def solved(pair):
    left, right = pair
    return (one_color(left, 'a') and one_color(right, 'b')) or (one_color(left, 'b') and one_color(right, 'a'))

def reduced(word):
    last = None
    for ch in word:
        if ch == last:
            return False
        last = ch
    return True

def children(pair):
    left, right = pair
    for x in range(len(left) + 1):
        for y in range(len(right) + 1):
            if x or y:
                yield x, y, (right[:y] + left[x:], left[:x] + right[y:])

def emit(goal, parent):
    moves = []
    state = goal
    while parent[state][0] is not None:
        prev, move = parent[state]
        moves.append(move)
        state = prev
    moves.reverse()
    result = [str(len(moves))]
    result += ["%d %d" % move for move in moves]
    print("\n".join(result))

def bfs(start, accept, keep):
    q = deque()
    q.append(start)
    parent = {start: (None, None)}
    while q:
        cur = q.popleft()
        for x, y, nxt in children(cur):
            if nxt in parent:
                continue
            parent[nxt] = (cur, (x, y))
            if accept(nxt):
                return nxt, parent
            if keep(nxt):
                q.append(nxt)
    return None, parent


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    solve()


