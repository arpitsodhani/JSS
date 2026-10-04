import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause army_power [Confidence: 0.80]
def army_power(cards):
    bonuses = []
    amount = 0
    for value in cards:
        if value:
            heapq.heappush(bonuses, -value)
        elif bonuses:
            amount -= heapq.heappop(bonuses)
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for cards in read_input():
        out.append(army_power(cards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

