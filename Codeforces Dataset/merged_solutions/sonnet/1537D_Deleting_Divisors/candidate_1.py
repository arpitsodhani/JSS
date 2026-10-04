import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: winner :: (n: int) -> str ---
def winner(n):
    if n % 2:
        return "Bob"
    power = 0
    value = n
    while value % 2 == 0:
        value //= 2
        power += 1
    if value > 1:
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
