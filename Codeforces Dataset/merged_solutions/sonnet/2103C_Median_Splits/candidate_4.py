import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        reader += 2
        cases.append((k, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: running_sums :: (k: int, a: list[int]) -> list[int] ---
def running_sums(k, a):
    sums = [0]
    for value in a:
        sums.append(sums[-1] + (1 if value <= k else -1))
    return sums


# --- clause: split_exists :: (sums: list[int]) -> bool ---
def split_exists(sums):
    n = len(sums) - 1
    total = sums[n]
    smallest = None
    for r in range(2, n):
        value = sums[r - 1]
        if value >= 0 and (smallest is None or value < smallest):
            smallest = value
        if smallest is not None and smallest <= sums[r]:
            return True
    first_good = None
    for l in range(1, n - 1):
        if sums[l] >= 0:
            first_good = l
            break
    if first_good is not None:
        for r in range(first_good + 1, n):
            if sums[r] <= total:
                return True
    lowest = None
    for r in range(2, n):
        value = sums[r - 1]
        if lowest is None or value < lowest:
            lowest = value
        if sums[r] <= total and lowest <= sums[r]:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append("YES" if split_exists(running_sums(k, a)) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
