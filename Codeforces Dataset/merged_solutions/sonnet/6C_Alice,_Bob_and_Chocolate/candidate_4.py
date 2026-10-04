import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: split_bars :: (times: list[int]) -> tuple[int, int] ---
def split_bars(times):
    start = 0
    right = len(times) - 1
    alice = 0
    bob = 0
    while start <= right:
        if alice <= bob:
            alice += times[start]
            start += 1
        else:
            bob += times[right]
            right -= 1
    return start, len(times) - start


# --- clause: main :: () -> None ---
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()
