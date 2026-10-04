import sys
from heapq import heappush, heappop

MOD = 10 ** 9 + 7


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    y = data[2]
    shows = []
    pos = 3
    for _ in range(n):
        shows.append((data[pos], data[pos + 1]))
        pos += 2
    return n, x, y, shows


# --- clause: total_cost :: (n: int, x: int, y: int, shows: list[tuple[int, int]]) -> int ---
def total_cost(n, x, y, shows):
    order = sorted(shows, key=lambda item: (item[0], item[1]))
    running = []
    idle = []
    spent = 0
    for start, finish in order:
        while running and running[0] < start:
            heappush(idle, -heappop(running))
        cheapest = x + y * (finish - start)
        if idle:
            last = -idle[0]
            reuse = y * (finish - last)
            if reuse <= cheapest:
                heappop(idle)
                cheapest = reuse
        spent += cheapest
        heappush(running, finish)
    return spent % MOD


# --- clause: main :: () -> None ---
def main():
    n, x, y, shows = read_input()
    sys.stdout.write(str(total_cost(n, x, y, shows)) + "\n")


if __name__ == "__main__":
    main()
