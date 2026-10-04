import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1]))
        pos += 2
    return cases

# --- clause: final_position :: (start: int, n: int) -> int ---
def final_position(start, n):
    left = n % 4
    first = n - left + 1
    position = start
    for step in range(left):
        jump = first + step
        if position & 1:
            position += jump
        else:
            position -= jump
    return position

# --- clause: main :: () -> None ---
def main():
    out = []
    for start, n in read_input():
        out.append(str(final_position(start, n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
