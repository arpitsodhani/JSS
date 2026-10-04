import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    k = data[0]
    n = data[1]
    return data[2:2 + k], data[2 + k:2 + k + n]

# Clause running_totals [Confidence: 1.00]
def running_totals(marks):
    totals = []
    carried = 0
    for element in marks:
        carried += element
        totals.append(carried)
    return sorted(set(totals))

# Clause count_starts [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    marks, scores = read_input()
    sys.stdout.write("%d\n" % count_starts(running_totals(marks), scores))


if __name__ == "__main__":
    main()

