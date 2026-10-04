import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        pos += 2
        cases.append((n, x))
    return cases


# --- clause: build_permutation :: (n: int, x: int) -> list[int] ---
def build_permutation(n, x):
    if x == n:
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
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
