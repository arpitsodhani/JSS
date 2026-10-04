import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    target = data[2]
    return n, k, target, data[3:3 + n]

# --- clause: half_counts :: (values: list[int], limit: int, target: int) -> list[dict] ---
def half_counts(values, limit, target):
    factorials = [1] * 20
    for i in range(1, 20):
        factorials[i] = factorials[i - 1] * i
    tables = [{0: 1}] + [{} for _ in range(limit)]
    for value in values:
        boost = factorials[value] if value < 20 else 0
        if boost > target:
            boost = 0
        fresh = []
        for used in range(limit + 1):
            layer = dict(tables[used])
            for total, count in tables[used].items():
                plain = total + value
                if plain <= target:
                    layer[plain] = layer.get(plain, 0) + count
            fresh.append(layer)
        if boost:
            for used in range(limit):
                layer = fresh[used + 1]
                for total, count in tables[used].items():
                    marked = total + boost
                    if marked <= target:
                        layer[marked] = layer.get(marked, 0) + count
        tables = fresh
    return tables

# --- clause: count_ways :: (n: int, k: int, target: int, a: list[int]) -> int ---
def count_ways(n, k, target, a):
    mid = n // 2
    left = half_counts(a[:mid], k, target)
    right = half_counts(a[mid:], k, target)
    total = 0
    for used_right in range(k + 1):
        table = right[used_right]
        if not table:
            continue
        for sum_right, count_right in table.items():
            need = target - sum_right
            if need < 0:
                continue
            for used_left in range(k - used_right + 1):
                found = left[used_left].get(need)
                if found:
                    total += count_right * found
    return total

# --- clause: main :: () -> None ---
def main():
    n, k, target, a = read_input()
    sys.stdout.write(str(count_ways(n, k, target, a)) + "\n")


if __name__ == "__main__":
    main()
