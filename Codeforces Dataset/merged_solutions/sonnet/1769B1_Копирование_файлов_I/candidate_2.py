import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: shared_percentages :: (sizes: list[int]) -> list[int] ---
def shared_percentages(sizes):
    total = sum(sizes)
    hit = [False] * 101
    hit[0] = True
    done = 0
    for size in sizes:
        for x in range(1, size + 1):
            here = 100 * x // size
            overall = 100 * (done + x) // total
            if here == overall:
                hit[here] = True
        done += size
    return [value for value in range(101) if hit[value]]


# --- clause: main :: () -> None ---
def main():
    sizes = read_input()
    sys.stdout.write("\n".join(map(str, shared_percentages(sizes))) + "\n")


if __name__ == "__main__":
    main()
