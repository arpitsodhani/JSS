import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: meeting_point :: (l: int, p: int, q: int) -> float ---
def meeting_point(l, p, q):
    time = l / (p + q)
    return p * time

# --- clause: main :: () -> None ---
def main():
    l, p, q = read_input()
    sys.stdout.write("%.10f\n" % meeting_point(l, p, q))


if __name__ == "__main__":
    main()
