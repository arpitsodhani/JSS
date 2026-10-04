import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append(tuple(data[1 + 4 * i:5 + 4 * i]))
    return cases


# --- clause: count_wins :: (a1: int, a2: int, b1: int, b2: int) -> int ---
def count_wins(a1, a2, b1, b2):
    wins = 0
    for mine in ((a1, a2), (a2, a1)):
        for theirs in ((b1, b2), (b2, b1)):
            score = 0
            for i in (0, 1):
                if mine[i] > theirs[i]:
                    score += 1
                elif mine[i] < theirs[i]:
                    score -= 1
            if score > 0:
                wins += 1
    return wins


# --- clause: main :: () -> None ---
def main():
    out = []
    for a1, a2, b1, b2 in read_input():
        out.append(count_wins(a1, a2, b1, b2))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
