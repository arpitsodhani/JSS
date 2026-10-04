import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases


# --- clause: enough_for :: (counts: list[int], k: int) -> bool ---
def enough_for(counts, k):
    left = counts[:]
    zeros = min(left[0], k)
    rest = k - zeros
    if left[1] < rest:
        return False
    left[0] -= zeros
    left[1] -= rest
    if left[0] + left[1] < rest:
        return False
    if left[0] >= rest:
        left[0] -= rest
    else:
        left[1] -= rest - left[0]
        left[0] = 0
    small = sum(left[:6])
    if small < k:
        return False
    need = k
    for digit in range(6):
        if not need:
            break
        used = min(left[digit], need)
        left[digit] -= used
        need -= used
    return sum(left) >= zeros + k


# --- clause: most_displays :: (s: str) -> int ---
def most_displays(s):
    counts = [0] * 10
    for code in s.encode():
        counts[code - 48] += 1
    best = 0
    low = 0
    high = len(s) // 4
    while low <= high:
        middle = (low + high) // 2
        if enough_for(counts, middle):
            best = middle
            low = middle + 1
        else:
            high = middle - 1
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(most_displays(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
