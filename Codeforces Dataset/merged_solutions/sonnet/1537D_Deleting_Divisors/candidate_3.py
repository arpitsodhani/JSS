import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: winner :: (n: int) -> str ---
def winner(n):
    if n % 2:
        return "Bob"
    power = 0
    element = n
    while element % 2 == 0:
        element //= 2
        power += 1
    if element > 1:
        return "Alice"
    if power % 2:
        return "Bob"
    return "Alice"


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(winner(n))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
