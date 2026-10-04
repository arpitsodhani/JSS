import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: steps_needed :: (a: list[int]) -> int ---
def steps_needed(a):
    return max(a) - min(a)


# --- clause: main :: () -> None ---
def main():
    written = []
    for a in read_input():
        written.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, written)) + "\n")


if __name__ == "__main__":
    main()
