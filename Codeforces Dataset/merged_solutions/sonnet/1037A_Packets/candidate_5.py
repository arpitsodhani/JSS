import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_packets :: (n: int) -> int ---
def fewest_packets(n):
    first_side = n
    packets = 0
    span = 1
    while first_side > 0:
        take = span if span < first_side else first_side
        first_side -= take
        span *= 2
        packets += 1
    return packets


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_packets(read_input()))


if __name__ == "__main__":
    main()
