import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: steps_needed :: (a: list[int]) -> int ---
def steps_needed(a):
    return max(a) - min(a)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
