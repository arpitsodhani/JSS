import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    pos = 2
    chains = []
    for _ in range(k):
        length = data[pos]
        pos += 1
        chains.append(data[pos:pos + length])
        pos += length
    return n, chains


# --- clause: seconds_needed :: (n: int, chains: list[list[int]]) -> int ---
def seconds_needed(n, chains):
    kept = 0
    for chain in chains:
        if chain[0] != 1:
            continue
        kept = 1
        while kept < len(chain) and chain[kept] == kept + 1:
            kept += 1
    k = len(chains)
    return 2 * n - k - 2 * kept + 1


# --- clause: main :: () -> None ---
def main():
    n, chains = read_input()
    sys.stdout.write("%d\n" % seconds_needed(n, chains))


if __name__ == "__main__":
    main()
