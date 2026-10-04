import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: group_order :: (a: list[int]) -> tuple[list[int], int] ---
def group_order(a):
    spots = {}
    for i in range(len(a)):
        if a[i] in spots:
            spots[a[i]].append(i)
        else:
            spots[a[i]] = [i]
    ranked = sorted(spots, key=lambda entry: -len(spots[entry]))
    order = []
    for entry in ranked:
        order.extend(spots[entry])
    return order, len(spots[ranked[0]])


# --- clause: shuffled :: (a: list[int], order: list[int], shift: int) -> list[int] ---
def shuffled(a, order, shift):
    n = len(a)
    out = [0] * n
    for i in range(n):
        out[order[i]] = a[order[(i + shift) % n]]
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        order, shift = group_order(a)
        out.append(" ".join(map(str, shuffled(a, order, shift))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
