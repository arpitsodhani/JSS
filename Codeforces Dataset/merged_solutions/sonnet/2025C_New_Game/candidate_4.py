import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        k = numbers[reader + 1]
        reader += 2
        cases.append((k, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: most_cards :: (k: int, a: list[int]) -> int ---
def most_cards(k, a):
    order = sorted(a)
    best = 0
    left = 0
    for right in range(len(order)):
        while order[right] - order[left] > k - 1:
            left += 1
        if right - left + 1 > best:
            best = right - left + 1
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(most_cards(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
