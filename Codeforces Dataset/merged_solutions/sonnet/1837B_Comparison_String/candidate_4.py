import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[2 + 2 * i].decode() for i in range(t)]


# --- clause: least_cost :: (s: str) -> int ---
def least_cost(s):
    runs = []
    run = 1
    spot = 1
    while spot < len(s):
        if s[spot] == s[spot - 1]:
            run += 1
        else:
            runs.append(run)
            run = 1
        spot += 1
    runs.append(run)
    return max(runs) + 1


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s in read_input():
        pieces.append(least_cost(s))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
