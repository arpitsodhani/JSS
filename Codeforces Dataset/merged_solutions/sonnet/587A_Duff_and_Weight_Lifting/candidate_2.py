import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: fewest_steps :: (powers: list[int]) -> int ---
def fewest_steps(powers):
    top = 1000000 + 25
    tally = [0] * (top + 2)
    for value in powers:
        tally[value] += 1
    steps = 0
    carry = 0
    for value in range(top + 1):
        here = tally[value] + carry
        steps += here & 1
        carry = here >> 1
    while carry:
        steps += carry & 1
        carry >>= 1
    return steps


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_steps(read_input()))


if __name__ == "__main__":
    main()
