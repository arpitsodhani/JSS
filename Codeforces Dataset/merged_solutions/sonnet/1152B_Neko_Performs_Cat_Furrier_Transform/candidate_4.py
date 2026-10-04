import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[-1])


# --- clause: plan_moves :: (x: int) -> tuple[int, list[int]] ---
def plan_moves(x):
    picks = []
    steps = 0
    while x & (x + 1):
        top = x.bit_length()
        gap = top - 1
        while gap >= 0 and x >> gap & 1:
            gap -= 1
        power = gap + 1
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
    start = read_input()
    steps, picks = plan_moves(start)
    sys.stdout.write(str(steps) + "\n" + " ".join(map(str, picks)) + "\n")


if __name__ == "__main__":
    main()
