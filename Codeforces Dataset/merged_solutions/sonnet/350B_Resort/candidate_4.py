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
    reach = [1] * (n + 1)
    for v in range(1, n + 1):
        u = source[v - 1]
        if u and kind[u - 1] == 0 and outdeg[u] == 1:
            reach[v] = reach[u] + 1
    top = 0
    end = 1
    for v in range(1, n + 1):
        if kind[v - 1] == 1 and reach[v] > top:
            top = reach[v]
            end = v
    path = [0] * top
    node = end
    for slot in range(top - 1, -1, -1):
        path[slot] = node
        node = source[node - 1]
    return path


# --- clause: main :: () -> None ---
def main():
    n, kind, source = read_input()
    path = longest_path(n, kind, source)
    sys.stdout.write(str(len(path)) + "\n" + " ".join(map(str, path)) + "\n")


if __name__ == "__main__":
    main()
