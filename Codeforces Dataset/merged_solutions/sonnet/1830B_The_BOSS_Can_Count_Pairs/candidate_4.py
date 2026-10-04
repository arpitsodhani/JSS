import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        a = numbers[reader:reader + n]
        reader += n
        b = numbers[reader:reader + n]
        reader += n
        cases.append((a, b))
    return cases


# --- clause: group_values :: (a: list[int], b: list[int]) -> dict[int, dict[int, int]] ---
def group_values(a, b):
    groups = {}
    for i in range(len(a)):
        row = groups.get(a[i])
        if row is None:
            row = {}
            groups[a[i]] = row
        row[b[i]] = row.get(b[i], 0) + 1
    return groups


# --- clause: count_pairs :: (n: int, groups: dict[int, dict[int, int]]) -> int ---
def count_pairs(n, groups):
    keys = sorted(groups)
    total = 0
    limit = 2 * n
    for i in range(len(keys)):
        x = keys[i]
        left = groups[x]
        for value in left:
            target = x * x
            other = target - value
            if other < value:
                continue
            if other == value:
                total += left[value] * (left[value] - 1) // 2
            elif other in left:
                total += left[value] * left[other]
        for j in range(i + 1, len(keys)):
            y = keys[j]
            if x * y > limit:
                break
            right = groups[y]
            small = left if len(left) <= len(right) else right
            big = right if small is left else left
            target = x * y
            for value in small:
                other = target - value
                if other in big:
                    total += small[value] * big[other]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(count_pairs(len(a), group_values(a, b)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
