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
        parent = source[v - 1]
        if parent:
            outdeg[parent] += 1
    best = []
    for hotel in range(1, n + 1):
        if kind[hotel - 1] == 0:
            continue
        walk = []
        node = hotel
        while True:
            walk.append(node)
            parent = source[node - 1]
            if parent == 0 or kind[parent - 1] == 1 or outdeg[parent] != 1:
                break
            node = parent
        if len(walk) > len(best):
            best = walk[::-1]
    return best


# --- clause: main :: () -> None ---
def main():
    n, kind, source = read_input()
    path = longest_path(n, kind, source)
    sys.stdout.write(str(len(path)) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()
