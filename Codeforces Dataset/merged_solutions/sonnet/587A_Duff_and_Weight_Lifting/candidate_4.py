import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: fewest_steps :: (powers: list[int]) -> int ---
def fewest_steps(powers):
    top = 1000000 + 25
    counts = [0] * (top + 2)
    for value in powers:
        counts[value] += 1
    steps = 0
    spot = 0
    carry = 0
    while spot <= top or carry:
        here = carry
        if spot <= top:
            here += counts[spot]
        if here % 2:
            steps += 1
        carry = here // 2
        spot += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_steps(read_input()))


if __name__ == "__main__":
    main()
