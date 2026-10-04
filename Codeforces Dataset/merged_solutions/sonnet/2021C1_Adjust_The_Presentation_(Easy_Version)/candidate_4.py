import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 3
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + m]
        pos += m
        cases.append((a, b))
    return cases


# --- clause: is_good :: (a: list[int], b: list[int]) -> bool ---
def is_good(a, b):
    n = len(a)
    m = len(b)
    first = [m + 1] * (n + 1)
    for index, member in enumerate(b):
        if first[member] > m:
            first[member] = index
    seen = -1
    for member in a:
        value = first[member]
        if value > m:
            continue
        if value < seen:
            return False
        seen = value
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append("YA" if is_good(a, b) else "TIDAK")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
