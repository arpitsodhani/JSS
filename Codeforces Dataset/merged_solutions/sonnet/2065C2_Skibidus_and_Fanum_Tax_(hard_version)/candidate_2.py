import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        m = tokens[at + 1]
        at += 2
        a = tokens[at:at + n]
        at += n
        b = tokens[at:at + m]
        at += m
        cases.append((a, b))
    return cases


# --- clause: can_sort :: (a: list[int], b: list[int]) -> bool ---
def can_sort(a, b):
    ranked = sorted(b)
    previous = -(1 << 62)
    for value in a:
        best = 1 << 62
        if value >= previous:
            best = value
        want = previous + value
        low = 0
        high = len(ranked)
        while low < high:
            mid = (low + high) // 2
            if ranked[mid] < want:
                low = mid + 1
            else:
                high = mid
        if low < len(ranked):
            flipped = ranked[low] - value
            if flipped < best:
                best = flipped
        if best == (1 << 62):
            return False
        previous = best
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append("YES" if can_sort(a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
