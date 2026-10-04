import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        d = numbers[reader + 1]
        reader += 2
        cases.append((d, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: rest_without :: (d: int, days: list[int], skip: int) -> int ---
def rest_without(d, days, skip):
    smallest = -1
    largest = 0
    previous = 0
    last = 0
    for i in range(len(days)):
        if i == skip:
            continue
        gap = days[i] - previous - 1
        if smallest < 0 or gap < smallest:
            smallest = gap
        if gap > largest:
            largest = gap
        previous = days[i]
        last = days[i]
    tail = d - last - 1
    inside = (largest - 1) // 2
    room = tail if tail > inside else inside
    return smallest if smallest < room else room


# --- clause: best_rest :: (d: int, days: list[int]) -> int ---
def best_rest(d, days):
    worst = 0
    smallest = days[0] - 1
    for i in range(1, len(days)):
        gap = days[i] - days[i - 1] - 1
        if gap < smallest:
            smallest = gap
            worst = i
    best = rest_without(d, days, worst)
    if worst > 0:
        other = rest_without(d, days, worst - 1)
        if other > best:
            best = other
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for d, days in read_input():
        out.append(best_rest(d, days))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
