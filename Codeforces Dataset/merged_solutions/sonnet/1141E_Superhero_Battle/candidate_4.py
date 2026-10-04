import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    hp = int(data[0])
    n = int(data[1])
    damage = [int(data[i + 2]) for i in range(n)]
    return hp, n, damage


# --- clause: prefix_stats :: (n: int, damage: list[int]) -> tuple[list[int], int, int] ---
def prefix_stats(n, damage):
    prefix = [0] * n
    running = 0
    lowest = 1 << 62
    for i in range(n):
        running = running + damage[i]
        prefix[i] = running
        if running < lowest:
            lowest = running
    return prefix, running, lowest


# --- clause: first_dead_minute :: (hp: int, n: int, prefix: list[int], total: int, lowest: int) -> int ---
def first_dead_minute(hp, n, prefix, total, lowest):
    if hp + lowest <= 0:
        rounds = 0
    else:
        if total >= 0:
            return -1
        rounds = (hp + lowest + (-total) - 1) // (-total)
    current = hp + rounds * total
    answer = -1
    for i in range(n):
        if current + prefix[i] <= 0:
            answer = rounds * n + i + 1
            break
    return answer


# --- clause: main :: () -> None ---
def main():
    hp, n, damage = read_input()
    prefix, total, lowest = prefix_stats(n, damage)
    answer = first_dead_minute(hp, n, prefix, total, lowest)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
