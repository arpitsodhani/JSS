import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases


# --- clause: order_pairs :: (a: list[int], b: list[int]) -> tuple[list[int], list[int]] ---
def order_pairs(a, b):
    n = len(a)
    slot = [0] * (n + 1)
    for index in range(n):
        slot[a[index]] = index
    first = []
    second = []
    for value in range(1, n + 1):
        index = slot[value]
        first.append(a[index])
        second.append(b[index])
    return first, second


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        first, second = order_pairs(a, b)
        out.append(" ".join(map(str, first)))
        out.append(" ".join(map(str, second)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
