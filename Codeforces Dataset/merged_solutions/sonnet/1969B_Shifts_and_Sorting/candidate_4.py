import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i] for i in range(t)]


# --- clause: sorting_cost :: (s: bytes) -> int ---
def sorting_cost(s):
    ones = 0
    total = 0
    for ch in s:
        if ch == 49:
            ones = ones + 1
        elif ones:
            total = total + ones + 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for word in read_input():
        out.append(str(sorting_cost(word)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
