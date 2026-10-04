import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return data[1:1 + t]


# --- clause: solve_case :: (n: int) -> str ---
def solve_case(n):
    if n % 2 == 0:
        return "-1"
    return " ".join(map(str, [n] + list(range(1, n))))


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    out = []
    for n in cases:
        out.append(solve_case(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
