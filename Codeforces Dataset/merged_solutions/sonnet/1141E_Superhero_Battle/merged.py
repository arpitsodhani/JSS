import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    hp = int(data[0])
    n = int(data[1])
    damage = list(map(int, data[2:2 + n]))
    return hp, n, damage

# Clause prefix_stats [Confidence: 0.80]
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

# Clause first_dead_minute [Confidence: 0.80]
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

# Clause main [Confidence: 1.00]
def main():
    hp, n, damage = read_input()
    prefix, total, lowest = prefix_stats(n, damage)
    sys.stdout.write(str(first_dead_minute(hp, n, prefix, total, lowest)) + "\n")


if __name__ == "__main__":
    main()

