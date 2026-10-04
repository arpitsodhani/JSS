import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(t)]


# --- clause: probes_needed :: (n: int, m: int) -> int ---
def probes_needed(n, m):
    if n == 1 and m == 1:
        return 0
    if n == 1 or m == 1:
        return 1
    return 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(str(probes_needed(n, m)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
