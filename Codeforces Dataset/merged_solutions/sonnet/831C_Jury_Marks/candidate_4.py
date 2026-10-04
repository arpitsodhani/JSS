import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    k = numbers[0]
    n = numbers[1]
    return numbers[2:2 + k], numbers[2 + k:2 + k + n]


# --- clause: running_totals :: (marks: list[int]) -> list[int] ---
def running_totals(marks):
    totals = []
    running = 0
    for entry in marks:
        running += entry
        totals.append(running)
    return sorted(set(totals))


# --- clause: count_starts :: (totals: list[int], scores: list[int]) -> int ---
def count_starts(totals, scores):
    known = set(totals)
    found = set()
    for step in totals:
        start = scores[0] - step
        if start in found:
            continue
        ok = True
        for value in scores:
            if value - start not in known:
                ok = False
                break
        if ok:
            found.add(start)
    return len(found)


# --- clause: main :: () -> None ---
def main():
    marks, scores = read_input()
    sys.stdout.write("%d\n" % count_starts(running_totals(marks), scores))


if __name__ == "__main__":
    main()
