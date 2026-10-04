import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: army_power :: (cards: list[int]) -> int ---
def army_power(cards):
    bonuses = []
    total = 0
    for value in cards:
        if value:
            heapq.heappush(bonuses, -value)
        elif bonuses:
            total -= heapq.heappop(bonuses)
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for cards in read_input():
        out.append(army_power(cards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
