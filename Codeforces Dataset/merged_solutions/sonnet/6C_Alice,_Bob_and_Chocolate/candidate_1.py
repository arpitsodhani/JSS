import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: split_bars :: (times: list[int]) -> tuple[int, int] ---
def split_bars(times):
    left = 0
    right = len(times) - 1
    alice = 0
    bob = 0
    while left <= right:
        if alice <= bob:
            alice += times[left]
            left += 1
        else:
            bob += times[right]
            right -= 1
    return left, len(times) - left


# --- clause: main :: () -> None ---
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()
