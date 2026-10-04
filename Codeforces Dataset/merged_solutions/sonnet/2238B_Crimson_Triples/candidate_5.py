import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[i]) for i in range(1, t + 1)]


# --- clause: count_triples :: (n: int) -> int ---
def count_triples(n):
    total = 0
    for b in range(n, 0, -1):
        share = n // b
        total += share * share
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(count_triples(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
