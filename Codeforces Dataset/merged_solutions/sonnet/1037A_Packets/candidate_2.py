import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_packets :: (n: int) -> int ---
def fewest_packets(n):
    low = n
    packets = 0
    width = 1
    while low > 0:
        take = width if width < low else low
        low -= take
        width *= 2
        packets += 1
    return packets


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_packets(read_input()))


if __name__ == "__main__":
    main()
