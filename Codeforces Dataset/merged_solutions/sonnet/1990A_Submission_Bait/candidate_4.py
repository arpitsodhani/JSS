import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: alice_wins :: (a: list[int]) -> bool ---
def alice_wins(a):
    tally = [0] * (len(a) + 1)
    for value in a:
        tally[value] += 1
    odd = 0
    for times in tally:
        odd += times % 2
    return odd > 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if alice_wins(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
