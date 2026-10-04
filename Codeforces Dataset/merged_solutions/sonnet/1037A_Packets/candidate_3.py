import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: fewest_packets :: (n: int) -> int ---
def fewest_packets(n):
    begin = n
    packets = 0
    extent = 1
    while begin > 0:
        take = extent if extent < begin else begin
        begin -= take
        extent *= 2
        packets += 1
    return packets


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_packets(read_input()))


if __name__ == "__main__":
    main()
