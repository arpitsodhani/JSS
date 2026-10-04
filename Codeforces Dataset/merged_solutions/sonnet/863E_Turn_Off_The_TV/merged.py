import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    spans = []
    for i in range(n):
        spans.append((data[1 + 2 * i], data[2 + 2 * i]))
    return spans

# Clause cover_counts [Confidence: 1.00]
def cover_counts(spans):
    points = set()
    for low, high in spans:
        points.add(low)
        points.add(high + 1)
    marks = sorted(points)
    place = {}
    for i in range(len(marks)):
        place[marks[i]] = i
    depth = [0] * (len(marks) + 1)
    for low, high in spans:
        depth[place[low]] += 1
        depth[place[high + 1]] -= 1
    carried = 0
    lonely = [0] * (len(marks) + 1)
    for i in range(len(marks)):
        carried += depth[i]
        width = marks[i + 1] - marks[i] if i + 1 < len(marks) else 0
        lonely[i + 1] = lonely[i] + (width if carried == 1 else 0)
    return marks, lonely

# Clause find_spare [Confidence: 0.80]
def find_spare(spans, marks, lonely):
    place = {}
    for i in range(len(marks)):
        place[marks[i]] = i
    for index in range(len(spans)):
        low, high = spans[index]
        left = place[low]
        right = place[high + 1]
        if lonely[right] - lonely[left] == 0:
            return index + 1
    return -1

# Clause main [Confidence: 1.00]
def main():
    spans = read_input()
    marks, lonely = cover_counts(spans)
    sys.stdout.write("%d\n" % find_spare(spans, marks, lonely))


if __name__ == "__main__":
    main()

