import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        q = fields[cursor + 1]
        cursor += 2
        a = fields[cursor:cursor + n]
        cursor += n
        asked = fields[cursor:cursor + q]
        cursor += q
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
        second_side = high
        while left < second_side:
            mid = (left + second_side) // 2
            if order[mid] <= middle:
                left = mid + 1
            else:
                second_side = mid
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
