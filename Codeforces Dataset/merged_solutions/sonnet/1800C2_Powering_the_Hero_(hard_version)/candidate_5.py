import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: army_power :: (cards: list[int]) -> int ---
def army_power(cards):
    bonuses = []
    amount = 0
    for value in cards:
        if value:
            heapq.heappush(bonuses, -value)
        elif bonuses:
            amount -= heapq.heappop(bonuses)
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for cards in read_input():
        out.append(army_power(cards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
