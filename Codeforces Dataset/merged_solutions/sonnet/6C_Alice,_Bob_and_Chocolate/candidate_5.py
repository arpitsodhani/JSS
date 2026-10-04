import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: split_bars :: (times: list[int]) -> tuple[int, int] ---
def split_bars(times):
    first_side = 0
    high = len(times) - 1
    alice = 0
    bob = 0
    while first_side <= high:
        if alice <= bob:
            alice += times[first_side]
            first_side += 1
        else:
            bob += times[high]
            high -= 1
    return first_side, len(times) - first_side


# --- clause: main :: () -> None ---
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()
