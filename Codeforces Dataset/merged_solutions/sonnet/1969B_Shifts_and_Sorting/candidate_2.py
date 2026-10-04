import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(data[1:1 + t])


# --- clause: sorting_cost :: (s: bytes) -> int ---
def sorting_cost(s):
    ones = 0
    total = 0
    for ch in s:
        if ch != 49:
            if ones > 0:
                total += ones + 1
        else:
            ones += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(sorting_cost(s)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
