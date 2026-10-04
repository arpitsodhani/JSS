import heapq
import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: carry_bits :: (a: list[int]) -> list[int] ---
def carry_bits(a):
    tally = {}
    for entry in a:
        tally[entry] = tally.get(entry, 0) + 1
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


# --- clause: missing_count :: (bits: list[int]) -> int ---
def missing_count(bits):
    have = set(bits)
    top = 0
    for power in have:
        if power > top:
            top = power
    return top + 1 - len(have)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % missing_count(carry_bits(read_input())))


if __name__ == "__main__":
    main()
