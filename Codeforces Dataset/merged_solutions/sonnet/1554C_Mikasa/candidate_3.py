import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: smallest_missing :: (n: int, m: int) -> int ---
def smallest_missing(n, m):
    target = m + 1
    reply = 0
    for bit in range(30, -1, -1):
        here = (n >> bit) & 1
        want = (target >> bit) & 1
        if here == want:
            continue
        if want:
            reply |= 1 << bit
        else:
            break
    return reply


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, m in read_input():
        pieces.append(smallest_missing(n, m))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
