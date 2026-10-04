import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: shared_percentages :: (sizes: list[int]) -> list[int] ---
def shared_percentages(sizes):
    total = sum(sizes)
    seen = [False] * 101
    seen[0] = True
    copied = 0
    for size in sizes:
        for byte in range(1, size + 1):
            copied += 1
            local = 100 * byte // size
            if local == 100 * copied // total:
                seen[local] = True
    return [value for value in range(101) if seen[value]]


# --- clause: main :: () -> None ---
def main():
    sizes = read_input()
    sys.stdout.write("\n".join(map(str, shared_percentages(sizes))) + "\n")


if __name__ == "__main__":
    main()
