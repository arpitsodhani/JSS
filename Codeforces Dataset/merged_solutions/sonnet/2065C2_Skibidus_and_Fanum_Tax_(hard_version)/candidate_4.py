import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        m = numbers[cursor + 1]
        cursor += 2
        a = numbers[cursor:cursor + n]
        cursor += n
        b = numbers[cursor:cursor + m]
        cursor += m
        cases.append((a, b))
    return cases


# --- clause: can_sort :: (a: list[int], b: list[int]) -> bool ---
def can_sort(a, b):
    ranked = sorted(b)
    reach = [1 << 62] * len(ranked)
    running = 1 << 62
    for i in range(len(ranked) - 1, -1, -1):
        if ranked[i] < running:
            running = ranked[i]
        reach[i] = running
    previous = -(1 << 62)
    for value in a:
        best = value if value >= previous else 1 << 62
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
            here = ranked[low] - value
            if here < best:
                best = here
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
