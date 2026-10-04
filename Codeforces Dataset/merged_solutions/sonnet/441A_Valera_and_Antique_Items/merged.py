import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    v = data[1]
    pos = 2
    sellers = []
    for _ in range(n):
        k = data[pos]
        pos += 1
        sellers.append(data[pos:pos + k])
        pos += k
    return n, v, sellers

# Clause reachable_sellers [Confidence: 0.60]
def reachable_sellers(v, sellers):
    good = []
    for index, prices in enumerate(sellers, start=1):
        if min(prices) < v:
            good.append(index)
    return good

# Clause main [Confidence: 1.00]
def main():
    n, v, sellers = read_input()
    good = reachable_sellers(v, sellers)
    sys.stdout.write(str(len(good)) + "\n" + " ".join(map(str, good)) + "\n")


if __name__ == "__main__":
    main()

