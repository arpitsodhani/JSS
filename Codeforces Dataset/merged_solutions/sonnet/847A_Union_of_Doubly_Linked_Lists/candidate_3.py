import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    prev = [0] * (n + 1)
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        prev[i] = fields[2 * i - 1]
        nxt[i] = fields[2 * i]
    return prev, nxt


# --- clause: join_lists :: (prev: list[int], nxt: list[int]) -> None ---
def join_lists(prev, nxt):
    n = len(prev) - 1
    known = [False] * (n + 1)
    tail = 0
    for v in range(1, n + 1):
        if known[v] or prev[v] != 0:
            continue
        read_at = v
        walk = v
        while walk:
            known[walk] = True
            last = walk
            walk = nxt[walk]
        if tail:
            nxt[tail] = read_at
            prev[read_at] = tail
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
