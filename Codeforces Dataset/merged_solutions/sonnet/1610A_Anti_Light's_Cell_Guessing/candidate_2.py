import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    numbers = list(map(int, data[1:1 + 2 * t]))
    return list(zip(numbers[0::2], numbers[1::2]))


# --- clause: probes_needed :: (n: int, m: int) -> int ---
def probes_needed(n, m):
    if n > 1 and m > 1:
        return 2
    if n > 1 or m > 1:
        return 1
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.append(str(probes_needed(n, m)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
