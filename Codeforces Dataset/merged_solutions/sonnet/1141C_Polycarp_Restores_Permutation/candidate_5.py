import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return n, raw[1:n]


# --- clause: restore :: (n: int, q: list[int]) -> list[int] | None ---
def restore(n, q):
    walk = [0]
    here = 0
    for step in q:
        here += step
        walk.append(here)
    shift = 1 - min(walk)
    p = [item + shift for item in walk]
    met = [False] * (n + 1)
    for item in p:
        if item < 1 or item > n or met[item]:
            return None
        met[item] = True
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
