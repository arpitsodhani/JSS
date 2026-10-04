import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]


# --- clause: pick_cars :: (v1: int, v2: int, v3: int, vm: int) -> tuple[int, int, int] | None ---
def pick_cars(v1, v2, v3, vm):
    small = v3 if v3 > vm else vm
    if small > 2 * v3 or small > 2 * vm:
        return None
    middle = v2 if v2 > 2 * vm else 2 * vm + 1
    if middle > 2 * v2 or middle <= small:
        return None
    big = v1 if v1 > middle else middle + 1
    if big > 2 * v1:
        return None
    return big, middle, small


# --- clause: main :: () -> None ---
def main():
    v1, v2, v3, vm = read_input()
    cars = pick_cars(v1, v2, v3, vm)
    if cars is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d\n%d\n%d\n" % cars)


if __name__ == "__main__":
    main()
