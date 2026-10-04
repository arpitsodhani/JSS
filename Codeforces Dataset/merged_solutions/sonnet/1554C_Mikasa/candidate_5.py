import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: smallest_missing :: (n: int, m: int) -> int ---
def smallest_missing(n, m):
    target = m + 1
    verdict = 0
    for bit in range(30, -1, -1):
        here = (n >> bit) & 1
        want = (target >> bit) & 1
        if here == want:
            continue
        if want:
            verdict |= 1 << bit
        else:
            break
    return verdict


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, m in read_input():
        lines.append(smallest_missing(n, m))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
