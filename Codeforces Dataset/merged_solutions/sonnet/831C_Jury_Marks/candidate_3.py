import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    k = fields[0]
    n = fields[1]
    return fields[2:2 + k], fields[2 + k:2 + k + n]


# --- clause: running_totals :: (marks: list[int]) -> list[int] ---
def running_totals(marks):
    totals = []
    carried = 0
    for element in marks:
        carried += element
        totals.append(carried)
    return sorted(set(totals))


# --- clause: count_starts :: (totals: list[int], scores: list[int]) -> int ---
def count_starts(totals, scores):
    known = set(totals)
    wanted = set(scores)
    found = set()
    first = scores[0]
    for step in totals:
        start = first - step
        if start in found:
            continue
        ok = True
        for element in wanted:
            if element - start not in known:
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
