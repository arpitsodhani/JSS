import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    hp = int(data[0])
    n = int(data[1])
    damage = [int(token) for token in data[2:n + 2]]
    return hp, n, damage


# --- clause: prefix_stats :: (n: int, damage: list[int]) -> tuple[list[int], int, int] ---
def prefix_stats(n, damage):
    prefix = [0] * n
    running = 0
    lowest = 0
    for i in range(n):
        running += damage[i]
        prefix[i] = running
        if i == 0 or running < lowest:
            lowest = running
    return prefix, running, lowest


# --- clause: first_dead_minute :: (hp: int, n: int, prefix: list[int], total: int, lowest: int) -> int ---
def first_dead_minute(hp, n, prefix, total, lowest):
    if hp + lowest <= 0:
        rounds = 0
    elif total >= 0:
        return -1
    else:
        rounds = -(-(hp + lowest) // -total)
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
