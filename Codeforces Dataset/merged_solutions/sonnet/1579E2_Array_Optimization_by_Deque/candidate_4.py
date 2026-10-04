import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = numbers[offset]
        offset += 1
        cases.append(numbers[offset:offset + n])
        offset += n
    return cases


# --- clause: fewest_inversions :: (a: list[int]) -> int ---
def fewest_inversions(a):
    import bisect

    seen = []
    total = 0
    for value in a:
        smaller = bisect.bisect_left(seen, value)
        bigger = len(seen) - bisect.bisect_right(seen, value)
        total += smaller if smaller < bigger else bigger
        bisect.insort(seen, value)
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_inversions(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
