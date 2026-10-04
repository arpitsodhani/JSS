import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    cursor = 1
    layers = []
    for _ in range(n):
        k = data[cursor]
        first_side = data[cursor + 1]
        second_side = data[cursor + 2]
        cursor += 3
        doors = data[cursor:cursor + k]
        cursor += k
        prefixes = [0]
        for length in doors:
            prefixes.append(prefixes[-1] + length)
        layers.append((first_side, second_side, prefixes))
    return layers

# Clause placeable [Confidence: 0.80]
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

# Clause widest_gap [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % widest_gap(read_input()))


if __name__ == "__main__":
    main()

