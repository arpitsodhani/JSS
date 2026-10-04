import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        m = raw[reader + 1]
        reader += 2
        a = raw[reader:reader + n]
        reader += n
        b = raw[reader:reader + m]
        reader += m
        cases.append((a, b))
    return cases


# --- clause: can_sort :: (a: list[int], b: list[int]) -> bool ---
def can_sort(a, b):
    ranked = sorted(b)
    previous = -(1 << 62)
    for value in a:
        top = 1 << 62
        if value >= previous:
            top = value
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
            if flipped < top:
                top = flipped
        if top == (1 << 62):
            return False
        previous = top
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append("YES" if can_sort(a, b) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
