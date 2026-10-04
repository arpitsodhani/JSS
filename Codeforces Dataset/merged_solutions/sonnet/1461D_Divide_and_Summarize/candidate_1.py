import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        q = data[pos + 1]
        pos += 2
        a = data[pos:pos + n]
        pos += n
        asked = data[pos:pos + q]
        pos += q
        cases.append((a, asked))
    return cases


# --- clause: reachable_sums :: (a: list[int]) -> set[int] ---
def reachable_sums(a):
    order = sorted(a)
    n = len(order)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + order[i]
    sums = set()
    stack = [(0, n)]
    while stack:
        low, high = stack.pop()
        sums.add(prefix[high] - prefix[low])
        if order[low] == order[high - 1]:
            continue
        middle = (order[low] + order[high - 1]) // 2
        left = low
        right = high
        while left < right:
            mid = (left + right) // 2
            if order[mid] <= middle:
                left = mid + 1
            else:
                right = mid
        stack.append((low, left))
        stack.append((left, high))
    return sums


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, asked in read_input():
        sums = reachable_sums(a)
        for value in asked:
            out.append("Yes" if value in sums else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
