# CLAUSE: setup_environment
import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    pos = 1
    weights = {}

# CLAUSE: solve_logic
    for _ in range(n):
        cost = int(data[pos])
        word = data[pos + 1]
        pos += 2
        letters = [x - 97 for x in word]
        if len(letters) < 2:
            continue
        graph = [set() for _ in range(12)]
        used = set(letters)
        bad = False
        for i in range(len(letters) - 1):
            a = letters[i]
            b = letters[i + 1]
            if a == b:
                bad = True
                break
            graph[a].add(b)
            graph[b].add(a)
        if bad:
            continue
        verts = [i for i in range(12) if graph[i] or i in used]
        edges = sum(len(x) for x in graph) // 2
        if edges != len(verts) - 1:
            continue
        if any(len(graph[i]) > 2 for i in verts):
            continue
        if len(verts) == 2:
            path = verts
        else:
            ends = [i for i in verts if len(graph[i]) == 1]
            if len(ends) != 2:
                continue
            path = []
            prev = -1
            cur = ends[0]
            while cur != -1:
                path.append(cur)
                nxt = -1
                for to in graph[cur]:
                    if to != prev:
                        nxt = to
                        break
                prev = cur
                cur = nxt
        one = tuple(path)
        two = tuple(reversed(path))
        key = one if one < two else two
        weights[key] = weights.get(key, 0) + cost

    child = []
    term = []

    def add_node():
        child.append({})
        term.append(0)
        return len(child) - 1

    add_node()
    for path, cost in weights.items():
        for seq in (path, tuple(reversed(path))):
            v = 0
            for ch in seq:
                nxt = child[v].get(ch)
                if nxt is None:
                    nxt = add_node()
                    child[v][ch] = nxt
                v = nxt
            term[v] += cost

    full = (1 << 12) - 1
    memo = {}
    take = {}

    def dp(mask, active):
        if mask == full:
            return 0
        state = (mask, active)
        if state in memo:
            return memo[state]
        best = -1
        best_ch = 0
        for ch in range(12):
            if mask & (1 << ch):
                continue
            nxt_active = []
            gain = 0
            root_next = child[0].get(ch)
            if root_next is not None:
                nxt_active.append(root_next)
                gain += term[root_next]
            for node in active:
                nxt = child[node].get(ch)
                if nxt is not None:
                    nxt_active.append(nxt)
                    gain += term[nxt]
            cur = gain + dp(mask | (1 << ch), tuple(nxt_active))
            if cur > best:
                best = cur
                best_ch = ch
        memo[state] = best
        take[state] = best_ch
        return best

    ans = []
    mask = 0
    active = ()
    for _ in range(12):
        dp(mask, active)
        ch = take[(mask, active)]
        ans.append(chr(97 + ch))
        nxt_active = []
        first = child[0].get(ch)
        if first is not None:
            nxt_active.append(first)
        for node in active:
            nxt = child[node].get(ch)
            if nxt is not None:
                nxt_active.append(nxt)
        mask |= 1 << ch
        active = tuple(nxt_active)

# CLAUSE: finish_program
    sys.stdout.write("".join(ans))

if __name__ == "__main__":
    main()
