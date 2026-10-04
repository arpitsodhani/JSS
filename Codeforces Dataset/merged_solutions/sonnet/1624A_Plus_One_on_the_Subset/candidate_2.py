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


# --- clause: steps_needed :: (a: list[int]) -> int ---
def steps_needed(a):
    return max(a) - min(a)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for a in read_input():
        lines.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()
