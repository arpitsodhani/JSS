import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: count_subsequences :: (a: list[int]) -> int ---
def count_subsequences(a):
    zeros = 0
    ones = 0
    for item in a:
        if item == 0:
            zeros += 1
        elif item == 1:
            ones += 1
    return ones * (1 << zeros)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(count_subsequences(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
