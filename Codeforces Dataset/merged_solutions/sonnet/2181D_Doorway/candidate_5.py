import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    offset = 1
    layers = []
    for _ in range(n):
        k = tokens[offset]
        left = tokens[offset + 1]
        right = tokens[offset + 2]
        offset += 3
        doors = tokens[offset:offset + k]
        offset += k
        prefixes = [0]
        for length in doors:
            prefixes.append(prefixes[-1] + length)
        layers.append((left, right, prefixes))
    return layers


# --- clause: placeable :: (layers: list[tuple[int, int, list[int]]], width: int) -> bool ---
def placeable(layers, width):
    events = []
    for left, right, prefixes in layers:
        room = right - left - prefixes[-1] - width
        if room < 0:
            return False
        from_here = -1
        stop = -1
        for shift in prefixes:
            here = left + shift
            if from_here < 0:
                from_here = here
                stop = here + room
            elif here <= stop:
                stop = here + room
            else:
                events.append((from_here, 1))
                events.append((stop + 1, -1))
                from_here = here
                stop = here + room
        events.append((from_here, 1))
        events.append((stop + 1, -1))
    events.sort()
    live = 0
    for _, delta in events:
        live += delta
        if live == len(layers):
            return True
    return False


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
