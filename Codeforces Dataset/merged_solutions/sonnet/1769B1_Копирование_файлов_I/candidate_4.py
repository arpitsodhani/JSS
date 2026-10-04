import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: shared_percentages :: (sizes: list[int]) -> list[int] ---
def shared_percentages(sizes):
    total = sum(sizes)
    marks = set([0])
    prefix = 0
    for size in sizes:
        for x in range(1, size + 1):
            local = 100 * x // size
            overall = 100 * (prefix + x) // total
            if local == overall:
                marks.add(local)
        prefix += size
    return sorted(marks)


# --- clause: main :: () -> None ---
def main():
    sizes = read_input()
    sys.stdout.write("\n".join(map(str, shared_percentages(sizes))) + "\n")


if __name__ == "__main__":
    main()
