# CLAUSE: setup_environment
import sys
from functools import lru_cache

def extract_path(raw):
    seq = [b - 97 for b in raw]
    if len(seq) <= 1:
        return None
    adj = [set() for _ in range(12)]
    present = set(seq)
    for a, b in zip(seq, seq[1:]):
        if a == b:
            return None
        adj[a].add(b)
        adj[b].add(a)
    vertices = [x for x in range(12) if x in present or adj[x]]
    if sum(len(adj[x]) for x in range(12)) // 2 != len(vertices) - 1:
        return None
    for x in vertices:
        if len(adj[x]) > 2:
            return None
    if len(vertices) == 2:
        route = vertices[:]
    else:
        ends = [x for x in vertices if len(adj[x]) == 1]
        if len(ends) != 2:
            return None
        route = []
        parent = -1
        node = ends[0]
        while node >= 0:
            route.append(node)
            candidates = [x for x in adj[node] if x != parent]
            parent, node = node, candidates[0] if candidates else -1
    route = tuple(route)
    other = route[::-1]
    return route if route < other else other

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    count = int(tokens[0])
    compressed = {}
    at = 1
    for _ in range(count):
        val = int(tokens[at])
        word = tokens[at + 1]
        at += 2
        path = extract_path(word)
        if path is not None:
            compressed[path] = compressed.get(path, 0) + val

    trie = [{}]
    finish = [0]
    for path, val in compressed.items():
        for direction in (path, path[::-1]):
            node = 0
            for letter in direction:
                edge = trie[node]
                if letter not in edge:
                    edge[letter] = len(trie)
                    trie.append({})
                    finish.append(0)
                node = edge[letter]
            finish[node] += val

    all_used = (1 << 12) - 1
    selected = {}

    @lru_cache(None)
    def solve(mask, live):
        if mask == all_used:
            return 0
        result = -1
        letter_choice = 0
        for letter in range(12):
            bit = 1 << letter
            if mask & bit:
                continue
            live_next = []
            gain = 0
            node = trie[0].get(letter)
            if node is not None:
                live_next.append(node)
                gain += finish[node]
            for old in live:
                node = trie[old].get(letter)
                if node is not None:
                    live_next.append(node)
                    gain += finish[node]
            value = gain + solve(mask | bit, tuple(live_next))
            if value > result:
                result = value
                letter_choice = letter
        selected[(mask, live)] = letter_choice
        return result

    mask = 0
    live = ()
    answer = []
    while mask != all_used:
        solve(mask, live)
        letter = selected[(mask, live)]
        answer.append(chr(letter + 97))
        live_next = []
        node = trie[0].get(letter)
        if node is not None:
            live_next.append(node)
        for old in live:
            node = trie[old].get(letter)
            if node is not None:
                live_next.append(node)
        live = tuple(live_next)
        mask |= 1 << letter

# CLAUSE: finish_program
    print("".join(answer))

if __name__ == "__main__":
    main()
