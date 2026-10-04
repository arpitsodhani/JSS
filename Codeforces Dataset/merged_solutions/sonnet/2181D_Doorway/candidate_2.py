import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    layers = []
    for _ in range(n):
        k = data[pos]
        begin = data[pos + 1]
        finish = data[pos + 2]
        pos += 3
        doors = data[pos:pos + k]
        pos += k
        prefixes = [0]
        for length in doors:
            prefixes.append(prefixes[-1] + length)
        layers.append((begin, finish, prefixes))
    return layers


# --- clause: placeable :: (layers: list[tuple[int, int, list[int]]], width: int) -> bool ---
def placeable(layers, width):
    events = []
    for begin, finish, prefixes in layers:
        room = finish - begin - prefixes[-1] - width
        if room < 0:
            return False
        start = -1
        stop = -1
        for shift in prefixes:
            here = begin + shift
            if start < 0:
                start = here
                stop = here + room
            elif here <= stop:
                stop = here + room
            else:
                events.append((start, 1))
                events.append((stop + 1, -1))
                start = here
                stop = here + room
        events.append((start, 1))
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
    for begin, finish, prefixes in layers:
        free = finish - begin - prefixes[-1]
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
