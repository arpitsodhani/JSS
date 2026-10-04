import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        k = raw[offset + 1]
        offset += 2
        cases.append((k, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: spin :: (k: int, a: list[int]) -> list[int] ---
def spin(k, a):
    n = len(a)
    seen = [False] * (n + 2)
    for number in a:
        seen[number] = True
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
