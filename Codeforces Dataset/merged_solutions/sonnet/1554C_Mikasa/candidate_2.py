import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: smallest_missing :: (n: int, m: int) -> int ---
def smallest_missing(n, m):
    target = m + 1
    result = 0
    for bit in range(30, -1, -1):
        here = (n >> bit) & 1
        want = (target >> bit) & 1
        if here == want:
            continue
        if want:
            result |= 1 << bit
        else:
            break
    return result


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(smallest_missing(n, m))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
