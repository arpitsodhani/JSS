import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: int_sqrt :: (value: int) -> int ---
def int_sqrt(value):
    root = int(value ** 0.5)
    while root * root > value:
        root -= 1
    while (root + 1) * (root + 1) <= value:
        root += 1
    return root


# --- clause: smallest_n :: (k: int) -> int ---
def smallest_n(k):
    low = 1
    upper = 2 * k + 2
    while low < upper:
        mid = (low + upper) // 2
        if mid - int_sqrt(mid) >= k:
            upper = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for k in read_input():
        pieces.append(smallest_n(k))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
