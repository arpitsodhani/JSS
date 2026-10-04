import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    prev = [0] * (n + 1)
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        prev[i] = raw[2 * i - 1]
        nxt[i] = raw[2 * i]
    return prev, nxt


# --- clause: join_lists :: (prev: list[int], nxt: list[int]) -> None ---
def join_lists(prev, nxt):
    n = len(prev) - 1
    visited = [False] * (n + 1)
    tail = 0
    for v in range(1, n + 1):
        if visited[v] or prev[v] != 0:
            continue
        taken = v
        walk = v
        while walk:
            visited[walk] = True
            last = walk
            walk = nxt[walk]
        if tail:
            nxt[tail] = taken
            prev[taken] = tail
        tail = last


# --- clause: main :: () -> None ---
def main():
    prev, nxt = read_input()
    join_lists(prev, nxt)
    out = []
    for i in range(1, len(prev)):
        out.append("%d %d" % (prev[i], nxt[i]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
