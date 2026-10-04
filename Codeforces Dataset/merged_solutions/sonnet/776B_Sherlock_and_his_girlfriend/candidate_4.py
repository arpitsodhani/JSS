import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: colour_prices :: (n: int) -> list[int] ---
def colour_prices(n):
    top = n + 1
    colours = [1] * (top + 1)
    step = 2
    while step * step <= top:
        multiple = step * step
        while multiple <= top:
            colours[multiple] = 2
            multiple += step
        step += 1
    return colours[2:top + 1]


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    colours = colour_prices(n)
    used = len(set(colours))
    sys.stdout.write("%d\n%s\n" % (used, " ".join(map(str, colours))))


if __name__ == "__main__":
    main()
