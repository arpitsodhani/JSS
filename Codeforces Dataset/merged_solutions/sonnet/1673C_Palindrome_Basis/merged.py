import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause palindromes_up_to [Confidence: 0.80]
def palindromes_up_to(limit):
    collected = []
    for entry in range(1, limit + 1):
        text = str(entry)
        if text == text[::-1]:
            collected.append(entry)
    return collected

# Clause partition_counts [Confidence: 1.00]
def partition_counts(limit):
    mod = 10 ** 9 + 7
    ways = [0] * (limit + 1)
    ways[0] = 1
    for entry in palindromes_up_to(limit):
        for total in range(entry, limit + 1):
            ways[total] = (ways[total] + ways[total - entry]) % mod
    return ways

# Clause main [Confidence: 1.00]
def main():
    cases = read_input()
    ways = partition_counts(max(cases))
    sys.stdout.write("\n".join(str(ways[n]) for n in cases) + "\n")


if __name__ == "__main__":
    main()

