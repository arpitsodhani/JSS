import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append(tuple(raw[1 + 4 * i:5 + 4 * i]))
    return cases


# --- clause: winner :: (a: int, b: int, c: int, d: int) -> str ---
def winner(a, b, c, d):
    mine = a if a < c else c
    theirs = b if b < d else d
    return "Gellyfish" if mine >= theirs else "Flower"


# --- clause: main :: () -> None ---
def main():
    written = []
    for a, b, c, d in read_input():
        written.append(winner(a, b, c, d))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
