import sys


# --- clause: read_input :: () -> tuple[int, list[int], int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    heroes = []
    for token in data[1:n + 1]:
        heroes.append(int(token))
    m = int(data[n + 1])
    dragons = [int(token) for token in data[n + 2:n + 2 + 2 * m]]
    return n, heroes, m, dragons


# --- clause: lower_bound :: (heroes: list[int], value: int) -> int ---
def lower_bound(heroes, value):
    low = 0
    high = len(heroes)
    while low < high:
        mid = (low + high) // 2
        if heroes[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low


# --- clause: dragon_cost :: (heroes: list[int], total: int, x: int, y: int) -> int ---
def dragon_cost(heroes, total, x, y):
    best = -1
    at = lower_bound(heroes, x)
    if at < len(heroes):
        rest = total - heroes[at]
        cost = 0
        if y > rest:
            cost = y - rest
        best = cost
    if at > 0:
        picked = heroes[at - 1]
        rest = total - picked
        cost = x - picked
        if y > rest:
            cost += y - rest
        if best < 0 or cost < best:
            best = cost
    return best


# --- clause: main :: () -> None ---
def main():
    n, heroes, m, dragons = read_input()
    heroes.sort()
    total = sum(heroes)
    out = []
    for i in range(m):
        out.append(str(dragon_cost(heroes, total, dragons[2 * i], dragons[2 * i + 1])))
    print("\n".join(out))


if __name__ == "__main__":
    main()
