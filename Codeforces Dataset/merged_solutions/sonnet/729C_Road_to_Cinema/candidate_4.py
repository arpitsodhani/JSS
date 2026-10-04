import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    s = numbers[2]
    t = numbers[3]
    cars = []
    reader = 4
    for _ in range(n):
        cars.append((numbers[reader], numbers[reader + 1]))
        reader += 2
    stations = sorted(numbers[reader:reader + k])
    return s, t, cars, stations


# --- clause: travel_time :: (tank: int, s: int, stations: list[int]) -> int ---
def travel_time(tank, s, stations):
    spots = [0] + stations + [s]
    gaps = []
    for i in range(1, len(spots)):
        gaps.append(spots[i] - spots[i - 1])
    widest = 0
    for gap in gaps:
        if gap > widest:
            widest = gap
    if tank < widest:
        return 1 << 62
    total = 0
    for gap in gaps:
        slow = gap - (tank - gap)
        if slow < 0:
            slow = 0
        total += gap + slow
    return total


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
