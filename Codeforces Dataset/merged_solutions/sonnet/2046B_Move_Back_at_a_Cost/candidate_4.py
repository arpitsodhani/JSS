import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: smallest_array :: (a: list[int]) -> list[int] ---
def smallest_array(a):
    n = len(a)
    best = 10 ** 18
    kept = []
    moved = []
    for i in range(n - 1, -1, -1):
        if a[i] > best:
            moved.append(a[i] + 1)
        else:
            kept.append(a[i])
            best = a[i]
    kept.reverse()
    if not moved:
        return kept
    moved.sort()
    limit = moved[0]
    front = []
    for value in kept:
        if value > limit:
            moved.append(value + 1)
        else:
            front.append(value)
    moved.sort()
    return front + moved


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, smallest_array(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
