import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(v) for v in data[1:t + 1]]


# --- clause: count_triples :: (n: int) -> int ---
def count_triples(n):
    total = 0
    for b in range(1, n + 1):
        share = n // b
        total = total + share * share
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for size in read_input():
        out.append(str(count_triples(size)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
