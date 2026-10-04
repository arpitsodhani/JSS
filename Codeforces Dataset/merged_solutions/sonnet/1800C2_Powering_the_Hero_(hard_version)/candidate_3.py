import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: army_power :: (cards: list[int]) -> int ---
def army_power(cards):
    bonuses = []
    summed = 0
    for value in cards:
        if value:
            heapq.heappush(bonuses, -value)
        elif bonuses:
            summed -= heapq.heappop(bonuses)
    return summed


# --- clause: main :: () -> None ---
def main():
    out = []
    for cards in read_input():
        out.append(army_power(cards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
