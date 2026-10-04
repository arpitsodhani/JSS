import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    made = list(map(int, data[2:m + 2]))
    return n, m, made


# --- clause: round_flags :: (n: int, m: int, made: list[int]) -> str ---
def round_flags(n, m, made):
    counts = [0] * (n + 1)
    ready = 0
    out = []
    for value in made:
        counts[value] += 1
        if counts[value] < 2:
            ready += 1
        if ready == n:
            out.append("1")
            ready = 0
            for level in range(1, n + 1):
                counts[level] -= 1
                if counts[level] > 0:
                    ready += 1
        else:
            out.append("0")
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    n, m, made = read_input()
    sys.stdout.write("%s\n" % round_flags(n, m, made))


if __name__ == "__main__":
    main()
