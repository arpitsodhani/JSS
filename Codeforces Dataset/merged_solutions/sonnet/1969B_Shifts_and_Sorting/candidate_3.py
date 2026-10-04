import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    words = []
    for i in range(t):
        words.append(data[1 + i])
    return words


# --- clause: sorting_cost :: (s: bytes) -> int ---
def sorting_cost(s):
    ones = 0
    total = 0
    for index in range(len(s)):
        ch = s[index]
        if ch == 49:
            ones += 1
        elif ones > 0:
            total += ones + 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(sorting_cost(s)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
