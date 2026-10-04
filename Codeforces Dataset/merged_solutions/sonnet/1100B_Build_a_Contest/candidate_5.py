import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    made = [int(token) for token in data[2:m + 2]]
    return n, m, made


# --- clause: round_flags :: (n: int, m: int, made: list[int]) -> str ---
def round_flags(n, m, made):
    counts = [0] * (n + 1)
    rounds = 0
    out = []
    for value in made:
        counts[value] += 1
        least = counts[1]
        for level in range(2, n + 1):
            if counts[level] < least:
                least = counts[level]
        if least > rounds:
            rounds = least
            out.append("1")
        else:
            out.append("0")
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    n, m, made = read_input()
    sys.stdout.write(round_flags(n, m, made) + "\n")


if __name__ == "__main__":
    main()
