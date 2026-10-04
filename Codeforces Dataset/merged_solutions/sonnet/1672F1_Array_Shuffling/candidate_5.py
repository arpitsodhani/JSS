import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: group_order :: (a: list[int]) -> tuple[list[int], int] ---
def group_order(a):
    spots = {}
    for i in range(0, len(a)):
        if a[i] in spots:
            spots[a[i]].append(i)
        else:
            spots[a[i]] = [i]
    ranked = sorted(spots, key=lambda item: -len(spots[item]))
    order = []
    for item in ranked:
        order.extend(spots[item])
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
