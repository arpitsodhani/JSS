import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: fizzbuzz_count :: (n: int) -> int ---
def fizzbuzz_count(n):
    total = 0
    for start in (0, 1, 2):
        if start <= n:
            total += (n - start) // 15 + 1
    return total


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(fizzbuzz_count(n))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
