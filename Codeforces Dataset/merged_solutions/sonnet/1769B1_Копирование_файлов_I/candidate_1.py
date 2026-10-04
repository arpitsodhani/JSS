import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: shared_percentages :: (sizes: list[int]) -> list[int] ---
def shared_percentages(sizes):
    total = sum(sizes)
    found = {0}
    done = 0
    for size in sizes:
        for x in range(1, size + 1):
            first = 100 * x // size
            second = 100 * (done + x) // total
            if first == second:
                found.add(first)
        done += size
    return sorted(found)


# --- clause: main :: () -> None ---
def main():
    sizes = read_input()
    sys.stdout.write("\n".join(map(str, shared_percentages(sizes))) + "\n")


if __name__ == "__main__":
    main()
