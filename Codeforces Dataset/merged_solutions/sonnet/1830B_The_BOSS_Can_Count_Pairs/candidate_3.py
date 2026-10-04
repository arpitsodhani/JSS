import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        a = fields[cursor:cursor + n]
        cursor += n
        b = fields[cursor:cursor + n]
        cursor += n
        cases.append((a, b))
    return cases


# --- clause: group_values :: (a: list[int], b: list[int]) -> dict[int, dict[int, int]] ---
def group_values(a, b):
    groups = {}
    for i in range(len(a)):
        entry_row = groups.get(a[i])
        if entry_row is None:
            entry_row = {}
            groups[a[i]] = entry_row
        entry_row[b[i]] = entry_row.get(b[i], 0) + 1
    return groups


# --- clause: count_pairs :: (n: int, groups: dict[int, dict[int, int]]) -> int ---
def count_pairs(n, groups):
    keys = sorted(groups)
    total = 0
    for i in range(len(keys)):
        x = keys[i]
        for j in range(i, len(keys)):
            y = keys[j]
            target = x * y
            if target > 2 * n:
                break
            left = groups[x]
            right = groups[y]
            if x == y:
                for value in left:
                    other = target - value
                    if other < value:
                        continue
                    if other == value:
                        total += left[value] * (left[value] - 1) // 2
                    elif other in left:
                        total += left[value] * left[other]
            else:
                if len(left) > len(right):
                    left, right = right, left
                for value in left:
                    other = target - value
                    if other in right:
                        total += left[value] * right[other]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(count_pairs(len(a), group_values(a, b)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
