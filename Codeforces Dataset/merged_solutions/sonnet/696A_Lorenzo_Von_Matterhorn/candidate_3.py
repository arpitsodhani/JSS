import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    q = fields[0]
    cursor = 1
    events = []
    for _ in range(q):
        if fields[cursor] == 1:
            events.append(fields[cursor:cursor + 4])
            cursor += 4
        else:
            events.append(fields[cursor:cursor + 3])
            cursor += 3
    return events


# --- clause: add_fee :: (fee: dict[int, int], u: int, v: int, w: int) -> None ---
def add_fee(fee, u, v, w):
    while u != v:
        if u > v:
            fee[u] = fee.get(u, 0) + w
            u //= 2
        else:
            fee[v] = fee.get(v, 0) + w
            v //= 2


# --- clause: path_fee :: (fee: dict[int, int], u: int, v: int) -> int ---
def path_fee(fee, u, v):
    tally = 0
    while u != v:
        if u > v:
            tally += fee.get(u, 0)
            u //= 2
        else:
            tally += fee.get(v, 0)
            v //= 2
    return tally


# --- clause: main :: () -> None ---
def main():
    fee = {}
    out = []
    for event in read_input():
        if event[0] == 1:
            add_fee(fee, event[1], event[2], event[3])
        else:
            out.append(path_fee(fee, event[1], event[2]))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
