import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append(tuple(tokens[1 + 4 * i:5 + 4 * i]))
    return cases


# --- clause: winner :: (a: int, b: int, c: int, d: int) -> str ---
def winner(a, b, c, d):
    mine = a if a < c else c
    theirs = b if b < d else d
    return "Gellyfish" if mine >= theirs else "Flower"


# --- clause: main :: () -> None ---
def main():
    lines = []
    for a, b, c, d in read_input():
        lines.append(winner(a, b, c, d))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
