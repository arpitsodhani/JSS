import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    reader = 1
    layers = []
    for _ in range(n):
        k = fields[reader]
        left = fields[reader + 1]
        right = fields[reader + 2]
        reader += 3
        doors = fields[reader:reader + k]
        reader += k
        prefixes = [0]
        for length in doors:
            prefixes.append(prefixes[-1] + length)
        layers.append((left, right, prefixes))
    return layers


# --- clause: placeable :: (layers: list[tuple[int, int, list[int]]], width: int) -> bool ---
def placeable(layers, width):
    spans = []
    for left, right, prefixes in layers:
        room = right - left - prefixes[-1] - width
        if room < 0:
            return False
        rows = []
        for shift in prefixes:
            here = left + shift
            if rows and here <= rows[-1][1]:
                rows[-1][1] = here + room
            else:
                rows.append([here, here + room])
        spans.append(rows)
    common = spans[0]
    for rows in spans[1:]:
        merged = []
        i = 0
        j = 0
        while i < len(common) and j < len(rows):
            low = common[i][0] if common[i][0] > rows[j][0] else rows[j][0]
            high = common[i][1] if common[i][1] < rows[j][1] else rows[j][1]
            if low <= high:
                merged.append([low, high])
            if common[i][1] < rows[j][1]:
                i += 1
            else:
                j += 1
        common = merged
        if not common:
            return False
    return len(common) > 0


# --- clause: widest_gap :: (layers: list[tuple[int, int, list[int]]]) -> int ---
def widest_gap(layers):
    low = 0
    high = 1 << 62
    for left, right, prefixes in layers:
        free = right - left - prefixes[-1]
        if free < high:
            high = free
    while low < high:
        mid = (low + high + 1) // 2
        if placeable(layers, mid):
            low = mid
        else:
            high = mid - 1
    return low


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % widest_gap(read_input()))


if __name__ == "__main__":
    main()
