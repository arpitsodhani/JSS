# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    s = data[0]
    t = data[1]
    start = (s, t)

    if solved(start):
        print(0)
        return

    total = len(s) + len(t)
    goal, parent = bfs(start, solved, lambda p: len(p[0]) + len(p[1]) == total and reduced(p[0]) and reduced(p[1]))
    if goal is not None:
        emit(goal, parent)
        return

    ca = s.count('a') + t.count('a')
    cb = total - ca
    final_a = ('a' * ca, 'b' * cb)
    final_b = ('b' * cb, 'a' * ca)
    goal, parent = bfs(start, lambda p: p == final_a or p == final_b, lambda p: True)
    if goal is not None:
        emit(goal, parent)

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
