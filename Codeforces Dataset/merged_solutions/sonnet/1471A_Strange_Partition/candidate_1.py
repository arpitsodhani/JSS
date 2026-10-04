import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((x, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: beauty_range :: (x: int, a: list[int]) -> tuple[int, int] ---
def beauty_range(x, a):
    total = 0
    spread = 0
    for value in a:
        total += value
        spread += (value + x - 1) // x
    return (total + x - 1) // x, spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append("%d %d" % beauty_range(x, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
