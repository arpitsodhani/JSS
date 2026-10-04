# CLAUSE: setup_environment
import sys

def canonical_pattern(word):
    letters = [x - 97 for x in word]
    if len(letters) <= 1:
        return ()
    masks = [0] * 12
    seen = 0
    for x in letters:
        seen |= 1 << x
    for i in range(1, len(letters)):
        a = letters[i - 1]
        b = letters[i]
        if a == b:
            return ()
        masks[a] |= 1 << b
        masks[b] |= 1 << a
    vertices = [i for i in range(12) if (seen >> i) & 1 or masks[i]]
    edge_total = sum(m.bit_count() for m in masks) // 2
    if edge_total != len(vertices) - 1:
        return ()
    if any(masks[i].bit_count() > 2 for i in vertices):
        return ()
    if len(vertices) == 2:
        path = tuple(vertices)
    else:
        ends = [i for i in vertices if masks[i].bit_count() == 1]
        if len(ends) != 2:
            return ()
        route = []
        prev = -1
        cur = ends[0]
        while cur != -1:
            route.append(cur)
            nxt = -1
            options = masks[cur] & ~(1 << prev) if prev >= 0 else masks[cur]
            if options:
                nxt = (options & -options).bit_length() - 1
            prev, cur = cur, nxt
        path = tuple(route)
    rev = path[::-1]
    return path if path < rev else rev

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    m = int(data[0])
    totals = {}
    j = 1
    for _ in range(m):
        cost = int(data[j])
        pattern = canonical_pattern(data[j + 1])
        j += 2
        if pattern:
            totals[pattern] = totals.get(pattern, 0) + cost

    nxt = [[-1] * 12]
    score = [0]

    def node():
        nxt.append([-1] * 12)
        score.append(0)
        return len(nxt) - 1

    for pattern, cost in totals.items():
        for seq in (pattern, pattern[::-1]):
            p = 0
            for letter in seq:
                q = nxt[p][letter]
                if q < 0:
                    q = node()
                    nxt[p][letter] = q
                p = q
            score[p] += cost

    target = (1 << 12) - 1
    memo = {}
    parent = {}

    def best(mask, active):
        if mask == target:
            return 0
        key = (mask, active)
        stored = memo.get(key)
        if stored is not None:
            return stored
        opt = -1
        opt_ch = 0
        for letter in range(12):
            if mask >> letter & 1:
                continue
            coming = []
            gain = 0
            root = nxt[0][letter]
            if root >= 0:
                coming.append(root)
                gain += score[root]
            for p in active:
                q = nxt[p][letter]
                if q >= 0:
                    coming.append(q)
                    gain += score[q]
            got = gain + best(mask | (1 << letter), tuple(coming))
            if got > opt:
                opt = got
                opt_ch = letter
        memo[key] = opt
        parent[key] = opt_ch
        return opt

    mask = 0
    active = ()
    out = []
    for _ in range(12):
        best(mask, active)
        letter = parent[(mask, active)]
        out.append(chr(97 + letter))
        coming = []
        root = nxt[0][letter]
        if root >= 0:
            coming.append(root)
        for p in active:
            q = nxt[p][letter]
            if q >= 0:
                coming.append(q)
        active = tuple(coming)
        mask |= 1 << letter

# CLAUSE: finish_program
    sys.stdout.write("".join(out) + "\n")

if __name__ == "__main__":
    main()
