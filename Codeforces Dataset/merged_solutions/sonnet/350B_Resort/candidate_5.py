import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    kind = data[1:1 + n]
    source = data[1 + n:1 + 2 * n]
    return n, kind, source


# --- clause: longest_path :: (n: int, kind: list[int], source: list[int]) -> list[int] ---
def longest_path(n, kind, source):
    outdeg = [0] * (n + 1)
    for v in range(1, n + 1):
        u = source[v - 1]
        if u:
            outdeg[u] += 1
    best = []
    v = 1
    while v <= n:
        if kind[v - 1] == 1:
            chain = [v]
            u = source[v - 1]
            while u != 0 and kind[u - 1] == 0 and outdeg[u] == 1:
                chain.append(u)
                u = source[u - 1]
            if len(chain) > len(best):
                best = list(reversed(chain))
        v += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, kind, source = read_input()
    path = longest_path(n, kind, source)
    sys.stdout.write(str(len(path)) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()
