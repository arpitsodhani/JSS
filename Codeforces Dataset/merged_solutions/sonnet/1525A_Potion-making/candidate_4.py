import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: fewest_steps :: (k: int) -> int ---
def fewest_steps(k):
    total = 1
    while k * total % 100:
        total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for k in read_input():
        pieces.append(fewest_steps(k))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
