import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: colour_prices :: (n: int) -> list[int] ---
def colour_prices(n):
    top = n + 1
    sieve = bytearray([1]) * (top + 1)
    sieve[0] = 0
    if top >= 1:
        sieve[1] = 0
    step = 2
    while step * step <= top:
        if sieve[step]:
            sieve[step * step::step] = bytearray(len(range(step * step, top + 1, step)))
        step += 1
    return [1 if sieve[value] else 2 for value in range(2, top + 1)]


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    colours = colour_prices(n)
    used = len(set(colours))
    sys.stdout.write("%d\n%s\n" % (used, " ".join(map(str, colours))))


if __name__ == "__main__":
    main()
