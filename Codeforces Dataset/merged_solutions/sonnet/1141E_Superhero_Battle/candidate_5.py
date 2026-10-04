import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    hp = int(data[0])
    n = int(data[1])
    damage = list(map(int, data[2:2 + n]))
    return hp, n, damage


# --- clause: prefix_stats :: (n: int, damage: list[int]) -> tuple[list[int], int, int] ---
def prefix_stats(n, damage):
    prefix = [0] * n
    acc = 0
    for i in range(n):
        acc += damage[i]
        prefix[i] = acc
    best = prefix[0]
    for i in range(1, n):
        if best > prefix[i]:
            best = prefix[i]
    return prefix, acc, best


# --- clause: first_dead_minute :: (hp: int, n: int, prefix: list[int], total: int, lowest: int) -> int ---
def first_dead_minute(hp, n, prefix, total, lowest):
    rounds = 0
    if hp + lowest > 0:
        if total >= 0:
            return -1
        rounds = -((hp + lowest) // total)
        while hp + rounds * total + lowest > 0:
            rounds += 1
    current = hp + rounds * total
    for i in range(n):
        if current + prefix[i] <= 0:
            return rounds * n + i + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    hp, n, damage = read_input()
    prefix, total, lowest = prefix_stats(n, damage)
    sys.stdout.write(str(first_dead_minute(hp, n, prefix, total, lowest)) + "\n")


if __name__ == "__main__":
    main()
