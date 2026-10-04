import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: winner :: (n: int) -> str ---
def winner(n):
    if n % 2:
        return "Bob"
    power = 0
    number = n
    while number % 2 == 0:
        number //= 2
        power += 1
    if number > 1:
        return "Alice"
    if power % 2:
        return "Bob"
    return "Alice"


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        lines.append(winner(n))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
