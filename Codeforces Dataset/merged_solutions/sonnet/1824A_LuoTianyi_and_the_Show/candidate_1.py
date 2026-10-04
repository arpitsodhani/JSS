import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        cases.append((n, m, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: best_seated :: (n: int, m: int, wishes: list[int]) -> int ---
def best_seated(n, m, wishes):
    fixed = sorted(set(v for v in wishes if v > 0))
    left_people = 0
    right_people = 0
    for value in wishes:
        if value == -1:
            left_people += 1
        elif value == -2:
            right_people += 1
    taken = [0] * (m + 2)
    for seat in fixed:
        taken[seat] = 1
    free_before = [0] * (m + 2)
    for seat in range(1, m + 1):
        free_before[seat] = free_before[seat - 1] + (0 if taken[seat] else 1)
    fixed_before = [0] * (m + 2)
    for seat in range(1, m + 1):
        fixed_before[seat] = fixed_before[seat - 1] + taken[seat]
    total_fixed = len(fixed)
    best = total_fixed

    def block_value(low, high):
        return (high - low + 1) + total_fixed - (fixed_before[high] - fixed_before[low - 1])

    for pivot in fixed:
        need = free_before[pivot - 1] - left_people
        low = 1
        high = pivot
        while low < high:
            middle = (low + high) // 2
            if free_before[middle - 1] >= need:
                high = middle
            else:
                low = middle + 1
        start = low
        limit = free_before[pivot] + right_people
        low = pivot
        high = m
        while low < high:
            middle = (low + high + 1) // 2
            if free_before[middle] <= limit:
                low = middle
            else:
                high = middle - 1
        stop = low
        value = block_value(start, stop)
        if value > best:
            best = value
    if left_people:
        need = free_before[m] - left_people
        low = 1
        high = m
        while low < high:
            middle = (low + high) // 2
            if free_before[middle - 1] >= need:
                high = middle
            else:
                low = middle + 1
        value = block_value(low, m)
        if value > best:
            best = value
    if right_people:
        low = 1
        high = m
        while low < high:
            middle = (low + high + 1) // 2
            if free_before[middle] <= right_people:
                low = middle
            else:
                high = middle - 1
        if free_before[low] <= right_people:
            value = block_value(1, low)
            if value > best:
                best = value
    return best if best < m else m


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, wishes in read_input():
        out.append(str(best_seated(n, m, wishes)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
