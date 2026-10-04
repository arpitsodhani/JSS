import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause balance_tables [Confidence: 1.00]
def balance_tables(s):
    n = len(s)
    running = [0] * (n + 1)
    for i in range(n):
        running[i + 1] = running[i] + (1 if s[i] == "(" else -1)
    lowest = [0] * (n + 2)
    lowest[n + 1] = 1 << 40
    for i in range(n, -1, -1):
        lowest[i] = running[i] if running[i] < lowest[i + 1] else lowest[i + 1]
    return running, lowest

# Clause count_flips [Confidence: 0.80]
def count_flips(s, running, lowest):
    n = len(s)
    amount = running[n]
    answer = 0
    floor = 0
    for i in range(n):
        if running[i] < floor:
            floor = running[i]
        if floor < 0:
            break
        if s[i] == "(":
            if amount == 2 and lowest[i + 1] >= 2:
                answer += 1
        else:
            if amount == -2 and lowest[i + 1] >= -2:
                answer += 1
    return answer

# Clause main [Confidence: 1.00]
def main():
    s = read_input()
    running, lowest = balance_tables(s)
    sys.stdout.write("%d\n" % count_flips(s, running, lowest))


if __name__ == "__main__":
    main()

