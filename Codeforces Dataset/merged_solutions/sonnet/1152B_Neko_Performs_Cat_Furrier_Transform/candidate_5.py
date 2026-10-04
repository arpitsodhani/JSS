import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: plan_moves :: (x: int) -> tuple[int, list[int]] ---
def plan_moves(x):
    steps = 0
    picks = []
    while x & (x + 1):
        gap = x.bit_length() - 1
        while gap >= 0 and (x >> gap) % 2 == 1:
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
    steps, picks = plan_moves(read_input())
    sys.stdout.write(str(steps) + "\n" + " ".join(map(str, picks)) + "\n")


if __name__ == "__main__":
    main()
