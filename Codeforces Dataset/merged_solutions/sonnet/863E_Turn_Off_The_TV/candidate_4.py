import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    spans = []
    for i in range(n):
        spans.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return spans


# --- clause: cover_counts :: (spans: list[tuple[int, int]]) -> tuple[list[int], list[int]] ---
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


# --- clause: find_spare :: (spans: list[tuple[int, int]], marks: list[int], lonely: list[int]) -> int ---
def find_spare(spans, marks, lonely):
    for index in range(len(spans)):
        low, high = spans[index]
        left = 0
        right = len(marks)
        while left < right:
            mid = (left + right) // 2
            if marks[mid] < low:
                left = mid + 1
            else:
                right = mid
        start = left
        left = 0
        right = len(marks)
        while left < right:
            mid = (left + right) // 2
            if marks[mid] < high + 1:
                left = mid + 1
            else:
                right = mid
        stop = left
        if lonely[stop] == lonely[start]:
            return index + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    spans = read_input()
    marks, lonely = cover_counts(spans)
    sys.stdout.write("%d\n" % find_spare(spans, marks, lonely))


if __name__ == "__main__":
    main()
