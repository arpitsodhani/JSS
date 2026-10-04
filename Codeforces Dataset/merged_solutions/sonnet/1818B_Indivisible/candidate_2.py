import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_permutation :: (n: int) -> list[int] | None ---
def build_permutation(n):
    if n == 1:
        return [1]
    if n & 1:
        return None
    order = list(range(1, n + 1))
    for i in range(0, n, 2):
        order[i], order[i + 1] = order[i + 1], order[i]
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        perm = build_permutation(n)
        if perm is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
