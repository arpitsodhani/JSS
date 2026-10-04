import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases


# --- clause: probes_needed :: (n: int, m: int) -> int ---
def probes_needed(n, m):
    if n * m == 1:
        return 0
    if n == 1 or m == 1:
        return 1
    return 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(str(probes_needed(n, m)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
