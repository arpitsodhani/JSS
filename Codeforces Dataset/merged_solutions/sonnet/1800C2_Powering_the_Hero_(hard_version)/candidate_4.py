import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: army_power :: (cards: list[int]) -> int ---
def army_power(cards):
    bonuses = []
    total = 0
    for value in cards:
        if value == 0:
            if bonuses:
                total += bonuses[0]
                bonuses[0] = bonuses[-1]
                bonuses.pop()
                spot = 0
                size = len(bonuses)
                while True:
                    best = spot
                    left = 2 * spot + 1
                    right = left + 1
                    if left < size and bonuses[left] > bonuses[best]:
                        best = left
                    if right < size and bonuses[right] > bonuses[best]:
                        best = right
                    if best == spot:
                        break
                    bonuses[spot], bonuses[best] = bonuses[best], bonuses[spot]
                    spot = best
            continue
        bonuses.append(value)
        spot = len(bonuses) - 1
        while spot and bonuses[(spot - 1) // 2] < bonuses[spot]:
            parent = (spot - 1) // 2
            bonuses[parent], bonuses[spot] = bonuses[spot], bonuses[parent]
            spot = parent
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for cards in read_input():
        out.append(army_power(cards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
