import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    hp, n = int(data[0]), int(data[1])
    damage = list(map(int, data[2:n + 2]))
    return hp, n, damage


# --- clause: prefix_stats :: (n: int, damage: list[int]) -> tuple[list[int], int, int] ---
def prefix_stats(n, damage):
    prefix = []
    running = 0
    for value in damage:
        running += value
        prefix.append(running)
    return prefix, prefix[-1], min(prefix)


# --- clause: first_dead_minute :: (hp: int, n: int, prefix: list[int], total: int, lowest: int) -> int ---
def first_dead_minute(hp, n, prefix, total, lowest):
    rounds = 0
    if hp + lowest > 0:
        if total >= 0:
            return -1
        need = hp + lowest
        step = -total
        rounds = need // step
        if need % step:
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
    sys.stdout.write("%d\n" % first_dead_minute(hp, n, prefix, total, lowest))


if __name__ == "__main__":
    main()
