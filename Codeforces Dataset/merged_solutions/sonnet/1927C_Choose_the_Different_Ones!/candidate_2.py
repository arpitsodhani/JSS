import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        m = tokens[pos + 1]
        k = tokens[pos + 2]
        pos += 3
        a = tokens[pos:pos + n]
        pos += n
        b = tokens[pos:pos + m]
        pos += m
        cases.append((k, a, b))
    return cases


# --- clause: can_pick :: (k: int, a: list[int], b: list[int]) -> bool ---
def can_pick(k, a, b):
    left = set(value for value in a if value <= k)
    high = set(value for value in b if value <= k)
    only_left = 0
    only_right = 0
    for value in range(1, k + 1):
        here = value in left
        there = value in high
        if not here and not there:
            return False
        if here and not there:
            only_left += 1
        elif there and not here:
            only_right += 1
    half = k // 2
    return only_left <= half and only_right <= half


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a, b in read_input():
        out.append("YES" if can_pick(k, a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
