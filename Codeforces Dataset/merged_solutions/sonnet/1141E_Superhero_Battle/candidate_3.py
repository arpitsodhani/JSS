import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    hp = int(data[0])
    n = int(data[1])
    damage = []
    for token in data[2:n + 2]:
        damage.append(int(token))
    return hp, n, damage


# --- clause: prefix_stats :: (n: int, damage: list[int]) -> tuple[list[int], int, int] ---
def prefix_stats(n, damage):
    prefix = [0] * n
    prefix[0] = damage[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + damage[i]
    lowest = prefix[0]
    for value in prefix:
        if value < lowest:
            lowest = value
    return prefix, prefix[n - 1], lowest


# --- clause: first_dead_minute :: (hp: int, n: int, prefix: list[int], total: int, lowest: int) -> int ---
def first_dead_minute(hp, n, prefix, total, lowest):
    if hp + lowest > 0 and total >= 0:
        return -1
    rounds = 0
    while hp + rounds * total + lowest > 0:
        gap = hp + rounds * total + lowest
        jump = (gap + (-total) - 1) // (-total)
        rounds += jump
    current = hp + rounds * total
    minute = 0
    while minute < n:
        if current + prefix[minute] <= 0:
            return rounds * n + minute + 1
        minute += 1
    return -1


# --- clause: main :: () -> None ---
def main():
    hp, n, damage = read_input()
    prefix, total, lowest = prefix_stats(n, damage)
    print(first_dead_minute(hp, n, prefix, total, lowest))


if __name__ == "__main__":
    main()
