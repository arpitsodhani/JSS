import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((int(data[2 * i + 1]), int(data[2 * i + 2])))
    return cases


# --- clause: probes_needed :: (n: int, m: int) -> int ---
def probes_needed(n, m):
    rows = 0 if n == 1 else 1
    cols = 0 if m == 1 else 1
    if rows and cols:
        return 2
    return rows + cols


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(str(probes_needed(n, m)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
