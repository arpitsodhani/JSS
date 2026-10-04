import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]

# Clause tally_shapes [Confidence: 1.00]
def tally_shapes(rows):
    opens = {}
    closes = {}
    for band in rows:
        balance = 0
        lowest = 0
        for ch in band:
            balance += 1 if ch == "(" else -1
            if balance < lowest:
                lowest = balance
        if lowest >= 0:
            opens[balance] = opens.get(balance, 0) + 1
        if lowest >= balance:
            closes[-balance] = closes.get(-balance, 0) + 1
    return opens, closes

# Clause count_pairs [Confidence: 0.80]
def count_pairs(opens, closes):
    amount = 0
    for value in opens:
        if value in closes:
            amount += opens[value] * closes[value]
    return amount

# Clause main [Confidence: 1.00]
def main():
    opens, closes = tally_shapes(read_input())
    sys.stdout.write("%d\n" % count_pairs(opens, closes))


if __name__ == "__main__":
    main()

