import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    arcs = []
    for i in range(m):
        arcs.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, m, arcs

# Clause augment [Confidence: 1.00]
def augment(n, adj, match_left, match_right, banned):
    came_from = [0] * (n + 1)
    reached = [False] * (n + 1)
    frontier = []
    for u in range(1, n + 1):
        if u != banned and not match_left[u] and adj[u]:
            frontier.append(u)
    at = 0
    while at < len(frontier):
        u = frontier[at]
        at += 1
        for w in adj[u]:
            if w == banned or reached[w]:
                continue
            reached[w] = True
            came_from[w] = u
            holder = match_right[w]
            if holder:
                frontier.append(holder)
                continue
            while w:
                owner = came_from[w]
                released = match_left[owner]
                match_left[owner] = w
                match_right[w] = owner
                w = released
            return True
    return False

# Clause full_matching [Confidence: 1.00]
def full_matching(n, adj):
    match_left = [0] * (n + 1)
    match_right = [0] * (n + 1)
    size = 0
    while augment(n, adj, match_left, match_right, 0):
        size += 1
    return size, match_left, match_right

# Clause best_center_score [Confidence: 1.00]
def best_center_score(n, adj, incident):
    total, base_left, base_right = full_matching(n, adj)
    best = 0
    for v in range(1, n + 1):
        match_left = base_left[:]
        match_right = base_right[:]
        size = total
        if match_left[v]:
            match_right[match_left[v]] = 0
            match_left[v] = 0
            size -= 1
        if match_right[v]:
            match_left[match_right[v]] = 0
            match_right[v] = 0
            size -= 1
        while size < total and augment(n, adj, match_left, match_right, v):
            size += 1
        score = incident[v] + size
        if score > best:
            best = score
    return best

# Clause solve [Confidence: 1.00]
def solve(n, m, arcs):
    adj = [[] for _ in range(n + 1)]
    incident = [0] * (n + 1)
    for a, b in arcs:
        adj[a].append(b)
        incident[a] += 1
        if b != a:
            incident[b] += 1
    return 3 * n - 2 + m - 2 * best_center_score(n, adj, incident)

# Clause main [Confidence: 1.00]
def main():
    n, m, arcs = read_input()
    sys.stdout.write(str(solve(n, m, arcs)) + "\n")


if __name__ == "__main__":
    main()

