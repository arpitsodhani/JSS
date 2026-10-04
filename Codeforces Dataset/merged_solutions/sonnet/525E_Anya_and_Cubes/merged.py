import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    target = data[2]
    return n, k, target, data[3:3 + n]

# Clause half_counts [Confidence: 1.00]
def half_counts(values, limit, target):
    tables = [{0: 1}]
    for _ in range(limit):
        tables.append({})
    for value in values:
        boost = 0
        if value <= 19:
            boost = 1
            for step in range(2, value + 1):
                boost *= step
            if boost > target:
                boost = 0
        fresh = [dict(part) for part in tables]
        for used in range(limit + 1):
            for total, count in tables[used].items():
                plain = total + value
                if plain <= target:
                    fresh[used][plain] = fresh[used].get(plain, 0) + count
                if boost and used < limit:
                    marked = total + boost
                    if marked <= target:
                        fresh[used + 1][marked] = fresh[used + 1].get(marked, 0) + count
        tables = fresh
    return tables

# Clause count_ways [Confidence: 1.00]
def count_ways(n, k, target, a):
    mid = n // 2
    left = half_counts(a[:mid], k, target)
    right = half_counts(a[mid:], k, target)
    total = 0
    for used_left in range(k + 1):
        table = left[used_left]
        if not table:
            continue
        room = k - used_left
        for sum_left, count_left in table.items():
            need = target - sum_left
            for used_right in range(room + 1):
                found = right[used_right].get(need)
                if found:
                    total += count_left * found
    return total

# Clause main [Confidence: 1.00]
def main():
    n, k, target, a = read_input()
    sys.stdout.write(str(count_ways(n, k, target, a)) + "\n")


if __name__ == "__main__":
    main()

