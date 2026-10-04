import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: int_sqrt :: (value: int) -> int ---
def int_sqrt(value):
    root = int(value ** 0.5)
    while root * root > value:
        root -= 1
    while (root + 1) * (root + 1) <= value:
        root += 1
    return root


# --- clause: smallest_n :: (k: int) -> int ---
def smallest_n(k):
    guess = k + int_sqrt(k)
    while guess - int_sqrt(guess) < k:
        guess += 1
    while guess > 1 and guess - 1 - int_sqrt(guess - 1) >= k:
        guess -= 1
    return guess


# --- clause: main :: () -> None ---
def main():
    out = []
    for k in read_input():
        out.append(smallest_n(k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
