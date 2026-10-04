import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    prev = [0 for _ in range(n + 1)]
    nxt = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        prev[i] = numbers[2 * i - 1]
        nxt[i] = numbers[2 * i]
    return prev, nxt


# --- clause: join_lists :: (prev: list[int], nxt: list[int]) -> None ---
def join_lists(prev, nxt):
    n = len(prev) - 1
    heads = []
    tails = []
    for v in range(1, n + 1):
        if prev[v] == 0:
            heads.append(v)
        if nxt[v] == 0:
            tails.append(v)
    heads.sort()
    order = []
    for head in heads:
        walk = head
        while walk:
            order.append(walk)
            walk = nxt[walk]
    for i in range(len(order)):
        v = order[i]
        prev[v] = order[i - 1] if i else 0
        nxt[v] = order[i + 1] if i + 1 < len(order) else 0


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
