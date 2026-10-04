# CLAUSE: setup_environment
import sys

ALPHA = 12

def add_pattern(store, cost, word):
    arr = [x - 97 for x in word]
    if len(arr) < 2:
        return
    neighbors = [[] for _ in range(ALPHA)]
    edge_seen = set()
    used = set(arr)
    for left, right in zip(arr, arr[1:]):
        if left == right:
            return
        a, b = (left, right) if left < right else (right, left)
        edge_seen.add((a, b))
    for a, b in edge_seen:
        neighbors[a].append(b)
        neighbors[b].append(a)
    verts = [i for i in range(ALPHA) if i in used or neighbors[i]]
    if len(edge_seen) != len(verts) - 1:
        return
    for v in verts:
        if len(neighbors[v]) > 2:
            return
    if len(verts) == 2:
        path = tuple(verts)
    else:
        starts = [v for v in verts if len(neighbors[v]) == 1]
        if len(starts) != 2:
            return
        cur = starts[0]
        prev = -1
        built = []
        while True:
            built.append(cur)
            nxt = -1
            for to in neighbors[cur]:
                if to != prev:
                    nxt = to
                    break
            if nxt < 0:
                break
            prev, cur = cur, nxt
        path = tuple(built)
    rev = path[::-1]
    key = path if path < rev else rev
    store[key] = store.get(key, 0) + cost

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    patterns = {}
    k = 1
    for _ in range(n):
        add_pattern(patterns, int(raw[k]), raw[k + 1])
        k += 2

    to = []
    end = []

    def create():
        to.append({})
        end.append(0)
        return len(to) - 1

    create()
    for path in patterns:
        weight = patterns[path]
        for s in (path, path[::-1]):
            v = 0
            for ch in s:
                if ch not in to[v]:
                    to[v][ch] = create()
                v = to[v][ch]
            end[v] += weight

    full = (1 << ALPHA) - 1
    dp = {}
    go = {}
    stack = [(0, (), 0)]
    while stack:
        mask, active, phase = stack.pop()
        state = (mask, active)
        if state in dp:
            continue
        if mask == full:
            dp[state] = 0
            continue
        if phase == 0:
            stack.append((mask, active, 1))
            for ch in range(ALPHA):
                if mask & (1 << ch):
                    continue
                live = []
                root = to[0].get(ch)
                if root is not None:
                    live.append(root)
                for node in active:
                    nxt = to[node].get(ch)
                    if nxt is not None:
                        live.append(nxt)
                child_state = (mask | (1 << ch), tuple(live))
                if child_state not in dp:
                    stack.append((child_state[0], child_state[1], 0))
        else:
            best_value = -1
            best_letter = 0
            for ch in range(ALPHA):
                if mask & (1 << ch):
                    continue
                live = []
                gain = 0
                root = to[0].get(ch)
                if root is not None:
                    live.append(root)
                    gain += end[root]
                for node in active:
                    nxt = to[node].get(ch)
                    if nxt is not None:
                        live.append(nxt)
                        gain += end[nxt]
                value = gain + dp[(mask | (1 << ch), tuple(live))]
                if value > best_value:
                    best_value = value
                    best_letter = ch
            dp[state] = best_value
            go[state] = best_letter

    mask = 0
    active = ()
    res = []
    for _ in range(ALPHA):
        ch = go[(mask, active)]
        res.append(chr(ch + 97))
        live = []
        root = to[0].get(ch)
        if root is not None:
            live.append(root)
        for node in active:
            nxt = to[node].get(ch)
            if nxt is not None:
                live.append(nxt)
        active = tuple(live)
        mask |= 1 << ch

# CLAUSE: finish_program
    print("".join(res))

if __name__ == "__main__":
    main()
