import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        x = int(data[pos])
        pos += 1
        y = int(data[pos])
        pos += 1
        a = data[pos]
        pos += 1
        b = data[pos]
        pos += 1
        cases.append((n, x, y, a, b))
    return cases


# --- clause: solve_case :: (n: int, x: int, y: int, a: bytes, b: bytes) -> int ---
def solve_case(n, x, y, a, b):
    spots = []
    for i in range(n):
        if a[i] == b[i]:
            continue
        spots.append(i)
    count = len(spots)
    if count % 2 == 1:
        return -1
    if count == 0:
        return 0
    if count == 2 and spots[1] == spots[0] + 1:
        cheapest = 2 * y
        if x < cheapest:
            cheapest = x
        return cheapest
    return (count // 2) * y


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2], case[3], case[4])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
