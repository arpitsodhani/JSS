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
    pairs = sorted(zip(a, b))
    first = [item[0] for item in pairs]
    second = [item[1] for item in pairs]
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
