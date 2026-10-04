import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: split_bars :: (times: list[int]) -> tuple[int, int] ---
def split_bars(times):
    low = 0
    right = len(times) - 1
    alice = 0
    bob = 0
    while low <= right:
        if alice <= bob:
            alice += times[low]
            low += 1
        else:
            bob += times[right]
            right -= 1
    return low, len(times) - low


# --- clause: main :: () -> None ---
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()
