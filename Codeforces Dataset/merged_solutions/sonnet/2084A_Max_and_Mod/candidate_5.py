import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    q = raw[0]
    return raw[1:1 + q]


# --- clause: solve_case :: (n: int) -> str ---
def solve_case(n):
    if n % 2 == 1:
        row = [str(n)]
        for v in range(1, n):
            row.append(str(v))
        return " ".join(row)
    return "-1"


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(solve_case(n))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
