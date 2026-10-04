import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: steps_needed :: (a: list[int]) -> int ---
def steps_needed(a):
    return max(a) - min(a)


# --- clause: main :: () -> None ---
def main():
    collected = []
    for a in read_input():
        collected.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()
