import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    for token in data[1:1 + t]:
        sizes.append(int(token))
    return sizes


# --- clause: count_triples :: (n: int) -> int ---
def count_triples(n):
    return sum((n // b) ** 2 for b in range(1, n + 1))


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(str(count_triples(n)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
