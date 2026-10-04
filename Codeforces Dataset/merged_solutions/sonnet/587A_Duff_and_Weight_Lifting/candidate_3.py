import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: fewest_steps :: (powers: list[int]) -> int ---
def fewest_steps(powers):
    top = 1000000 + 25
    occurrences = [0] * (top + 2)
    for entry in powers:
        occurrences[entry] += 1
    steps = 0
    carry = 0
    for entry in range(top + 1):
        here = occurrences[entry] + carry
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
