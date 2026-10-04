import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: is_shuffle :: (a: list[int]) -> bool ---
def is_shuffle(a):
    n = len(a)
    visited = [False] * n
    for k in range(n):
        spot = (k + a[k]) % n
        if visited[spot]:
            return False
        visited[spot] = True
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if is_shuffle(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
