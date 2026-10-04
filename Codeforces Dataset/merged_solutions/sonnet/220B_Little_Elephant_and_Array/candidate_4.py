import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    a = numbers[2:2 + n]
    asked = []
    reader = 2 + n
    for _ in range(m):
        asked.append((numbers[reader], numbers[reader + 1]))
        reader += 2
    return a, asked


# --- clause: candidate_spots :: (a: list[int]) -> dict[int, list[int]] ---
def candidate_spots(a):
    n = len(a)
    counts = [0] * (n + 2)
    for value in a:
        if value <= n:
            counts[value] += 1
    spots = {}
    for value in range(1, n + 1):
        if counts[value] >= value:
            spots[value] = []
    for i in range(n):
        value = a[i]
        if value <= n and value in spots:
            spots[value].append(i)
    return spots


# --- clause: answer_queries :: (spots: dict[int, list[int]], asked: list[tuple[int, int]]) -> list[int] ---
def answer_queries(spots, asked):
    out = []
    for low, high in asked:
        total = 0
        for value in spots:
            places = spots[value]
            left = 0
            right = len(places)
            while left < right:
                mid = (left + right) // 2
                if places[mid] < low - 1:
                    left = mid + 1
                else:
                    right = mid
            start = left
            left = 0
            right = len(places)
            while left < right:
                mid = (left + right) // 2
                if places[mid] < high:
                    left = mid + 1
                else:
                    right = mid
            if left - start == value:
                total += 1
        out.append(total)
    return out


# --- clause: main :: () -> None ---
def main():
    a, asked = read_input()
    spots = candidate_spots(a)
    sys.stdout.write("\n".join(map(str, answer_queries(spots, asked))) + "\n")


if __name__ == "__main__":
    main()
