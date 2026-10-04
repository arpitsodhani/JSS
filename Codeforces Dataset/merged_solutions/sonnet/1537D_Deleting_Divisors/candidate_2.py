import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: winner :: (n: int) -> str ---
def winner(n):
    if n % 2:
        return "Bob"
    power = 0
    item = n
    while item % 2 == 0:
        item //= 2
        power += 1
    if item > 1:
        return "Alice"
    if power % 2:
        return "Bob"
    return "Alice"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(winner(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
