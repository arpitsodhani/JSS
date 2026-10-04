import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause carry_bits [Confidence: 1.00]
def carry_bits(a):
    tally = {}
    for element in a:
        tally[element] = tally.get(element, 0) + 1
    heap = list(tally)
    heapq.heapify(heap)
    bits = []
    while heap:
        power = heapq.heappop(heap)
        times = tally.pop(power, 0)
        if times == 0:
            continue
        if times % 2:
            bits.append(power)
        carry = times // 2
        if carry:
            if power + 1 in tally:
                tally[power + 1] += carry
            else:
                tally[power + 1] = carry
                heapq.heappush(heap, power + 1)
    return bits

# Clause missing_count [Confidence: 0.80]
def missing_count(bits):
    return bits[-1] + 1 - len(bits)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % missing_count(carry_bits(read_input())))


if __name__ == "__main__":
    main()

