import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    k = raw[1]
    s = raw[2]
    t = raw[3]
    cars = []
    offset = 4
    for _ in range(n):
        cars.append((raw[offset], raw[offset + 1]))
        offset += 2
    stations = sorted(raw[offset:offset + k])
    return s, t, cars, stations


# --- clause: travel_time :: (tank: int, s: int, stations: list[int]) -> int ---
def travel_time(tank, s, stations):
    spots = [0] + stations + [s]
    running = 0
    for i in range(1, len(spots)):
        gap = spots[i] - spots[i - 1]
        if tank < gap:
            return 1 << 62
        fast = tank - gap
        if fast > gap:
            fast = gap
        running += 2 * gap - fast
    return running


# --- clause: cheapest_car :: (s: int, t: int, cars: list[tuple[int, int]], stations: list[int]) -> int ---
def cheapest_car(s, t, cars, stations):
    low = 1
    high = 2 * s
    while low < high:
        mid = (low + high) // 2
        if travel_time(mid, s, stations) <= t:
            high = mid
        else:
            low = mid + 1
    if travel_time(low, s, stations) > t:
        return -1
    best = -1
    for price, tank in cars:
        if tank >= low and (best < 0 or price < best):
            best = price
    return best


# --- clause: main :: () -> None ---
def main():
    s, t, cars, stations = read_input()
    sys.stdout.write("%d\n" % cheapest_car(s, t, cars, stations))


if __name__ == "__main__":
    main()
