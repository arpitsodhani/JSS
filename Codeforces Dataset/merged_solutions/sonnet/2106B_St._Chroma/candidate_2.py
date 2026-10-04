import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n, x = int(data[idx]), int(data[idx + 1])
        idx += 2
        cases.append((n, x))
    return cases


# --- clause: build_permutation :: (n: int, x: int) -> list[int] ---
def build_permutation(n, x):
    if x == n:
        return list(range(n))
    order = list(range(x))
    order += list(range(x + 1, n))
    order.append(x)
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x in read_input():
        out.append(" ".join(map(str, build_permutation(n, x))))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
