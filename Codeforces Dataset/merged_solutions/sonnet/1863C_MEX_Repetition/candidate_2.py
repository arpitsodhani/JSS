import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        k = tokens[pos + 1]
        pos += 2
        cases.append((k, tokens[pos:pos + n]))
        pos += n
    return cases


# --- clause: spin :: (k: int, a: list[int]) -> list[int] ---
def spin(k, a):
    n = len(a)
    seen = [False] * (n + 2)
    for item in a:
        seen[item] = True
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
