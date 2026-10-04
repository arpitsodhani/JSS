import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        x = raw[offset + 1]
        offset += 2
        cases.append((x, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: beauty_range :: (x: int, a: list[int]) -> tuple[int, int] ---
def beauty_range(x, a):
    total = 0
    spread = 0
    for number in a:
        total += number
        spread += (number + x - 1) // x
    return (total + x - 1) // x, spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, a in read_input():
        out.append("%d %d" % beauty_range(x, a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
