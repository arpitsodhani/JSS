import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        k = fields[cursor + 1]
        cursor += 2
        cases.append((k, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: spin :: (k: int, a: list[int]) -> list[int] ---
def spin(k, a):
    n = len(a)
    seen = [False] * (n + 2)
    for element in a:
        seen[element] = True
    missing = 0
    while seen[missing]:
        missing += 1
    circle = a + [missing]
    shift = k % (n + 1)
    if shift:
        circle = circle[-shift:] + circle[:-shift]
    return circle[:n]


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(" ".join(map(str, spin(k, a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
