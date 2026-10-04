import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        q = numbers[reader + 1]
        reader += 2
        a = numbers[reader:reader + n]
        reader += n
        asked = numbers[reader:reader + q]
        reader += q
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
    layer = [(0, n)]
    while layer:
        fresh = []
        for low, high in layer:
            sums.add(prefix[high] - prefix[low])
            if order[low] == order[high - 1]:
                continue
            middle = (order[low] + order[high - 1]) // 2
            cut = low
            step = high - low
            while step:
                while cut + step <= high and order[cut + step - 1] <= middle:
                    cut += step
                step //= 2
            fresh.append((low, cut))
            fresh.append((cut, high))
        layer = fresh
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
