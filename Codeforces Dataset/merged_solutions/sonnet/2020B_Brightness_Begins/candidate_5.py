import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


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
    floor_value = 1
    ceiling_value = 2 * k + 2
    while floor_value < ceiling_value:
        mid = (floor_value + ceiling_value) // 2
        if mid - int_sqrt(mid) >= k:
            ceiling_value = mid
        else:
            floor_value = mid + 1
    return floor_value


# --- clause: main :: () -> None ---
def main():
    out = []
    for k in read_input():
        out.append(smallest_n(k))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
