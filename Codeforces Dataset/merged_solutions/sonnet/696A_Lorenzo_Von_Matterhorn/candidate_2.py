import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    q = tokens[0]
    pos = 1
    events = []
    for _ in range(q):
        if tokens[pos] == 1:
            events.append(tokens[pos:pos + 4])
            pos += 4
        else:
            events.append(tokens[pos:pos + 3])
            pos += 3
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
    amount = 0
    while u != v:
        if u > v:
            amount += fee.get(u, 0)
            u //= 2
        else:
            amount += fee.get(v, 0)
            v //= 2
    return amount


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
