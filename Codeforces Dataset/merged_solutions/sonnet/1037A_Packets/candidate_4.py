import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_packets :: (n: int) -> int ---
def fewest_packets(n):
    packets = 0
    reach = 0
    size = 1
    while reach < n:
        reach += size
        size *= 2
        packets += 1
    return packets


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_packets(read_input()))


if __name__ == "__main__":
    main()
