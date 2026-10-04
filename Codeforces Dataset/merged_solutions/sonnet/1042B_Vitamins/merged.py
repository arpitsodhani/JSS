import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    juices = []
    for i in range(n):
        price = int(data[1 + 2 * i])
        mask = 0
        for letter in data[2 + 2 * i]:
            mask |= 1 << (letter - 65)
        juices.append((price, mask))
    return juices

# Clause cheapest_set [Confidence: 1.00]
def cheapest_set(juices):
    infinity = float("inf")
    cost = [infinity] * 8
    cost[0] = 0
    for price, flags in juices:
        for have in range(8):
            if cost[have] == infinity:
                continue
            summed = cost[have] + price
            if summed < cost[have | flags]:
                cost[have | flags] = summed
    return -1 if cost[7] == infinity else cost[7]

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % cheapest_set(read_input()))


if __name__ == "__main__":
    main()

