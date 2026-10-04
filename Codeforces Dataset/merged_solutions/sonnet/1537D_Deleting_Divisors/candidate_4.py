import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: winner :: (n: int) -> str ---
def winner(n):
    if n % 2 == 1:
        return "Bob"
    power = 1
    steps = 0
    while power < n:
        power *= 2
        steps += 1
    if power != n:
        return "Alice"
    return "Alice" if steps % 2 == 0 else "Bob"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(winner(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
