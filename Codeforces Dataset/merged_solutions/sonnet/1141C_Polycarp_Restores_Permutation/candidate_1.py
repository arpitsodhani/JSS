import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:n]


# --- clause: restore :: (n: int, q: list[int]) -> list[int] | None ---
def restore(n, q):
    walk = [0]
    here = 0
    for step in q:
        here += step
        walk.append(here)
    shift = 1 - min(walk)
    p = [value + shift for value in walk]
    seen = [False] * (n + 1)
    for value in p:
        if value < 1 or value > n or seen[value]:
            return None
        seen[value] = True
    return p


# --- clause: main :: () -> None ---
def main():
    n, q = read_input()
    p = restore(n, q)
    if p is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, p)) + "\n")


if __name__ == "__main__":
    main()
