import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    la = data[0]
    lb = data[1]
    a = data[2:2 + la]
    b = data[2 + la:2 + la + lb]
    return la, lb, a, b


# --- clause: longest_run :: (la: int, lb: int, a: list[int], b: list[int]) -> int ---
def longest_run(la, lb, a, b):
    place = {}
    for index in range(lb):
        place[b[index]] = index
    spots = []
    for value in a:
        spots.append(place[value] if value in place else -1)
    cap = la if la < lb else lb
    best = 0
    left = 0
    weight = 0
    for right in range(2 * la):
        here = spots[right % la]
        if here < 0:
            left = right + 1
            weight = 0
            continue
        if right > left:
            before = spots[(right - 1) % la]
            gap = here - before
            if gap <= 0:
                gap += lb
            weight += gap
            while weight >= lb:
                first = spots[left % la]
                second = spots[(left + 1) % la]
                back = second - first
                if back <= 0:
                    back += lb
                weight -= back
                left += 1
        while right - left + 1 > cap:
            first = spots[left % la]
            second = spots[(left + 1) % la]
            back = second - first
            if back <= 0:
                back += lb
            weight -= back
            left += 1
        span = right - left + 1
        if span > best:
            best = span
    return best


# --- clause: main :: () -> None ---
def main():
    la, lb, a, b = read_input()
    sys.stdout.write(str(longest_run(la, lb, a, b)) + "\n")


if __name__ == "__main__":
    main()
