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


# --- clause: verdict :: (a: list[int]) -> str ---
def verdict(a):
    total = 0
    for value in a:
        total ^= value
    if total == 0:
        return "DRAW"
    bit = total.bit_length() - 1
    mine = 0
    for value in a:
        if (value >> bit) & 1:
            mine += 1
    rest = len(a) - mine
    if mine % 4 == 1:
        return "WIN"
    return "WIN" if rest % 2 == 1 else "LOSE"


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(verdict(a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
