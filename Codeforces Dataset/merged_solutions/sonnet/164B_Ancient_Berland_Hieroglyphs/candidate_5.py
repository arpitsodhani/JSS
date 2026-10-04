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
    where = {}
    for index, value in enumerate(b):
        where[value] = index
    spots = [where.get(value, -1) for value in a]
    cap = min(la, lb)
    best = 0
    left = 0
    used = 0
    total = 2 * la
    for right in range(total):
        here = spots[right % la]
        if here < 0:
            left = right + 1
            used = 0
            continue
        if right > left:
            previous = spots[(right - 1) % la]
            step = here - previous
            if step <= 0:
                step += lb
            used += step
            while used > lb - 1:
                gone = spots[left % la]
                nxt = spots[(left + 1) % la]
                back = nxt - gone
                if back <= 0:
                    back += lb
                used -= back
                left += 1
        length = right - left + 1
        if length > cap:
            left += 1
            length = right - left + 1
            gone = spots[(left - 1) % la]
            nxt = spots[left % la]
            back = nxt - gone
            if back <= 0:
                back += lb
            used -= back
        if length > best:
            best = length
    return best


# --- clause: main :: () -> None ---
def main():
    la, lb, a, b = read_input()
    sys.stdout.write(str(longest_run(la, lb, a, b)) + "\n")


if __name__ == "__main__":
    main()
