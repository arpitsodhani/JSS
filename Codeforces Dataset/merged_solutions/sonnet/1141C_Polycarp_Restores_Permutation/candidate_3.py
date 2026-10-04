import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return n, fields[1:n]


# --- clause: restore :: (n: int, q: list[int]) -> list[int] | None ---
def restore(n, q):
    walk = [0]
    here = 0
    for step in q:
        here += step
        walk.append(here)
    shift = 1 - min(walk)
    p = [entry + shift for entry in walk]
    marked = [False] * (n + 1)
    for entry in p:
        if entry < 1 or entry > n or marked[entry]:
            return None
        marked[entry] = True
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
