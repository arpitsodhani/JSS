import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    return x


# --- clause: plan_moves :: (x: int) -> tuple[int, list[int]] ---
def plan_moves(x):
    steps = 0
    picks = []
    while x & (x + 1):
        power = 0
        for bit in range(x.bit_length() - 1, -1, -1):
            if not x >> bit & 1:
                power = bit + 1
                break
        x ^= (1 << power) - 1
        picks.append(power)
        steps += 1
        if x & (x + 1) == 0:
            break
        x += 1
        steps += 1
    return steps, picks


# --- clause: main :: () -> None ---
def main():
    steps, picks = plan_moves(read_input())
    sys.stdout.write("%d\n%s\n" % (steps, " ".join(map(str, picks))))


if __name__ == "__main__":
    main()
