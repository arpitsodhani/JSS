import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[i]), int(data[i + 1])) for i in range(1, 2 * t + 1, 2)]


# --- clause: probes_needed :: (n: int, m: int) -> int ---
def probes_needed(n, m):
    if n == 1 and m == 1:
        return 0
    if min(n, m) == 1:
        return 1
    return 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(probes_needed(case[0], case[1])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
