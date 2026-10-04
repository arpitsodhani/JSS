import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: good_order :: (a: list[int]) -> list[int] ---
def good_order(a):
    buckets = {}
    for value in a:
        buckets[value] = buckets.get(value, 0) + 1
    out = []
    for value in range(max(a), 0, -1):
        for _ in range(buckets.get(value, 0)):
            out.append(value)
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, good_order(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
