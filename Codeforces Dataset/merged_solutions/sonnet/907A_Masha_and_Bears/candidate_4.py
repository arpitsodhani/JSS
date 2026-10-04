import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3]


# --- clause: pick_cars :: (v1: int, v2: int, v3: int, vm: int) -> tuple[int, int, int] | None ---
def pick_cars(v1, v2, v3, vm):
    for small in range(v3, 2 * v3 + 1):
        if small < vm or small > 2 * vm:
            continue
        for middle in range(2 * vm + 1, 2 * v2 + 1):
            if middle < v2 or middle <= small:
                continue
            for big in range(middle + 1, 2 * v1 + 1):
                if big >= v1:
                    return big, middle, small
    return None


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
