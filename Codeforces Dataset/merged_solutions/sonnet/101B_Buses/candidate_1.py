import sys

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    buses = []
    pos = 2
    for _ in range(m):
        buses.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, buses


# --- clause: count_routes :: (n: int, buses: list[tuple[int, int]]) -> int ---
def count_routes(n, buses):
    stops = sorted({0} | {t for _s, t in buses})
    index = {}
    for position, stop in enumerate(stops):
        index[stop] = position
    size = len(stops)
    ways = [0] * size
    ways[0] = 1
    prefix = [0] * (size + 1)
    prefix[1] = 1
    order = sorted(buses, key=lambda bus: bus[1])
    at = 0
    filled = 1
    while at < len(order):
        finish = order[at][1]
        gained = 0
        while at < len(order) and order[at][1] == finish:
            start = order[at][0]
            at += 1
            low = 0
            high = filled
            while low < high:
                middle = (low + high) // 2
                if stops[middle] < start:
                    low = middle + 1
                else:
                    high = middle
            gained += prefix[filled] - prefix[low]
        spot = index[finish]
        ways[spot] = (ways[spot] + gained) % MOD
        while filled <= spot:
            prefix[filled + 1] = (prefix[filled] + ways[filled]) % MOD
            filled += 1
    return ways[index[n]] % MOD if n in index else 0


# --- clause: main :: () -> None ---
def main():
    n, m, buses = read_input()
    sys.stdout.write(str(count_routes(n, buses)) + "\n")


if __name__ == "__main__":
    main()
