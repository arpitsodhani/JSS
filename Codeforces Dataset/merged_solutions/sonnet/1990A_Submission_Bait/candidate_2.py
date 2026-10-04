import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: alice_wins :: (a: list[int]) -> bool ---
def alice_wins(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    for value in tally:
        if tally[value] % 2:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if alice_wins(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
