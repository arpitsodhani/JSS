import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(v) for v in data[1:t + 1]]


# --- clause: moves_needed :: (n: int) -> int ---
def moves_needed(n):
    twos = 0
    threes = 0
    while not n % 2:
        n = n // 2
        twos = twos + 1
    while n % 3 == 0:
        n //= 3
        threes += 1
    if n != 1 or threes < twos:
        return -1
    return 2 * threes - twos


# --- clause: main :: () -> None ---
def main():
    out = []
    for value in read_input():
        out.append(str(moves_needed(value)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
