import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    r = data[2]
    buy = data[3:3 + n]
    sell = data[3 + n:3 + n + m]
    return n, m, r, buy, sell

# Clause best_money [Confidence: 0.80]
def best_money(r, buy, sell):
    cheapest = min(buy)
    dearest = max(sell)
    if dearest <= cheapest:
        return r
    shares = r // cheapest
    return r - shares * cheapest + shares * dearest

# Clause main [Confidence: 1.00]
def main():
    n, m, r, buy, sell = read_input()
    sys.stdout.write(str(best_money(r, buy, sell)) + "\n")


if __name__ == "__main__":
    main()

