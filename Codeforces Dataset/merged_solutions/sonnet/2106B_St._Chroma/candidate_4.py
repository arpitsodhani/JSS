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
        pos += 1
        x = int(data[pos])
        pos += 1
        cases.append((n, x))
    return cases


# --- clause: build_permutation :: (n: int, x: int) -> list[int] ---
def build_permutation(n, x):
    if x == n:
        return list(range(n))
    order = []
    for value in range(x):
        order.append(value)
    for value in range(x + 1, n):
        order.append(value)
    order.append(x)
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(" ".join(map(str, build_permutation(case[0], case[1]))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
