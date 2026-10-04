import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: split_bars :: (times: list[int]) -> tuple[int, int] ---
def split_bars(times):
    begin = 0
    stop = len(times) - 1
    alice = 0
    bob = 0
    while begin <= stop:
        if alice <= bob:
            alice += times[begin]
            begin += 1
        else:
            bob += times[stop]
            stop -= 1
    return begin, len(times) - begin


# --- clause: main :: () -> None ---
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()
