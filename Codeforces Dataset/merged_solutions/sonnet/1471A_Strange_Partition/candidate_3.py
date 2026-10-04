import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        x = fields[cursor + 1]
        cursor += 2
        cases.append((x, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: beauty_range :: (x: int, a: list[int]) -> tuple[int, int] ---
def beauty_range(x, a):
    total = 0
    spread = 0
    for element in a:
        total += element
        spread += (element + x - 1) // x
    return (total + x - 1) // x, spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append("%d %d" % beauty_range(x, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
