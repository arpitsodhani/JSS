import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        x = int(data[pos + 1])
        pos += 2
        cases.append((n, x))
    return cases


# --- clause: build_permutation :: (n: int, x: int) -> list[int] ---
def build_permutation(n, x):
    if n == x:
        return list(range(n))
    order = list(range(x))
    order.extend(range(x + 1, n))
    order.append(x)
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x in read_input():
        out.append(" ".join(map(str, build_permutation(n, x))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
