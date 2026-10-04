import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    cursor = 2
    chains = []
    for _ in range(k):
        length = numbers[cursor]
        cursor += 1
        chains.append(numbers[cursor:cursor + length])
        cursor += length
    return n, chains


# --- clause: seconds_needed :: (n: int, chains: list[list[int]]) -> int ---
def seconds_needed(n, chains):
    kept = 0
    unpack = 0
    for chain in chains:
        unpack += len(chain) - 1
        if chain[0] == 1:
            kept = 1
            i = 1
            while i < len(chain) and chain[i] == chain[i - 1] + 1:
                kept += 1
                i += 1
    return unpack - (kept - 1) + (n - kept)


# --- clause: main :: () -> None ---
def main():
    n, chains = read_input()
    sys.stdout.write("%d\n" % seconds_needed(n, chains))


if __name__ == "__main__":
    main()
