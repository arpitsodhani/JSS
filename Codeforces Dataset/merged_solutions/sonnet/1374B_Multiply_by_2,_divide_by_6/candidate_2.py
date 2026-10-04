import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(map(int, data[1:1 + t]))


# --- clause: moves_needed :: (n: int) -> int ---
def moves_needed(n):
    twos = 0
    threes = 0
    while n % 2 == 0:
        n //= 2
        twos += 1
    while n % 3 == 0:
        n //= 3
        threes += 1
    if n > 1:
        return -1
    if twos > threes:
        return -1
    return threes + (threes - twos)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(moves_needed(n)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
