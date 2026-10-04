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


# --- clause: least_sum :: (x: list[int]) -> int ---
def least_sum(x):
    values = list(x)
    while True:
        top = max(values)
        low = min(values)
        if top == low:
            return top * len(values)
        for i in range(len(values)):
            if values[i] == top:
                values[i] = top % low if top % low else low


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % least_sum(read_input()))


if __name__ == "__main__":
    main()
