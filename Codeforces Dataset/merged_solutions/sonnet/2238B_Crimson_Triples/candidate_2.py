import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(map(int, data[1:1 + t]))


# --- clause: count_triples :: (n: int) -> int ---
def count_triples(n):
    total = 0
    b = 1
    while b <= n:
        share = n // b
        total += share * share
        b += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(count_triples(n)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
