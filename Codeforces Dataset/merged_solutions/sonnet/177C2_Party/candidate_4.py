import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pos = 2
    friends = []
    for _ in range(k):
        friends.append((data[pos], data[pos + 1]))
        pos += 2
    m = data[pos]
    pos += 1
    foes = []
    for _ in range(m):
        foes.append((data[pos], data[pos + 1]))
        pos += 2
    return n, friends, foes


# --- clause: largest_party :: (n: int, friends: list[tuple[int, int]], foes: list[tuple[int, int]]) -> int ---
def largest_party(n, friends, foes):
    adj = [[] for _ in range(n + 1)]
    for a, b in friends:
        adj[a].append(b)
        adj[b].append(a)
    component = [0] * (n + 1)
    members = [[]]
    for start in range(1, n + 1):
        if component[start]:
            continue
        label = len(members)
        bucket = []
        queue = [start]
        component[start] = label
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            bucket.append(node)
            for nxt in adj[node]:
                if not component[nxt]:
                    component[nxt] = label
                    queue.append(nxt)
        members.append(bucket)
    bad = set()
    for a, b in foes:
        if component[a] == component[b]:
            bad.add(component[a])
    best = 0
    for label in range(1, len(members)):
        if label not in bad and len(members[label]) > best:
            best = len(members[label])
    return best


# --- clause: main :: () -> None ---
def main():
    n, friends, foes = read_input()
    sys.stdout.write(str(largest_party(n, friends, foes)) + "\n")


if __name__ == "__main__":
    main()
