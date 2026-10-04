import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: shared_percentages :: (sizes: list[int]) -> list[int] ---
def shared_percentages(sizes):
    total = sum(sizes)
    found = set()
    found.add(0)
    done = 0
    for size in sizes:
        x = 1
        while x <= size:
            first = 100 * x // size
            if first == 100 * (done + x) // total:
                found.add(first)
            x += 1
        done += size
    answer = list(found)
    answer.sort()
    return answer


# --- clause: main :: () -> None ---
def main():
    sizes = read_input()
    sys.stdout.write("\n".join(map(str, shared_percentages(sizes))) + "\n")


if __name__ == "__main__":
    main()
