import heapq
import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: carry_bits :: (a: list[int]) -> list[int] ---
def carry_bits(a):
    tally = {}
    for number in a:
        tally[number] = tally.get(number, 0) + 1
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
    return bits[-1] + 1 - len(bits)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % missing_count(carry_bits(read_input())))


if __name__ == "__main__":
    main()
