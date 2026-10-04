import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    s = data[1].decode()
    q = int(data[2])
    asked = []
    for i in range(q):
        asked.append((int(data[3 + 2 * i]), data[4 + 2 * i].decode()))
    return s, asked

# Clause best_runs [Confidence: 1.00]
def best_runs(s):
    n = len(s)
    tables = []
    for letter in range(26):
        ch = chr(97 + letter)
        best = [0] * (n + 1)
        for left in range(n):
            cost = 0
            for right in range(left, n):
                if s[right] != ch:
                    cost += 1
                if cost <= n and right - left + 1 > best[cost]:
                    best[cost] = right - left + 1
        for budget in range(1, n + 1):
            if best[budget - 1] > best[budget]:
                best[budget] = best[budget - 1]
        tables.append(best)
    return tables

# Clause main [Confidence: 1.00]
def main():
    s, asked = read_input()
    tables = best_runs(s)
    out = []
    for budget, ch in asked:
        table = tables[ord(ch) - 97]
        spot = budget if budget < len(table) - 1 else len(table) - 1
        out.append(table[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

