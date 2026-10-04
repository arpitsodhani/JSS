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


# --- clause: fewest_changes :: (a: list[int]) -> int ---
def fewest_changes(a):
    n = len(a)
    ranked = sorted(a)
    widest = 2
    for right in range(2, n):
        low = 0
        high = right - 1
        while low < high:
            mid = (low + high) // 2
            if ranked[mid] + ranked[mid + 1] > ranked[right]:
                high = mid
            else:
                low = mid + 1
        if right - low + 1 > widest:
            widest = right - low + 1
    return n - widest


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(fewest_changes(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
