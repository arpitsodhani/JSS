import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    a = tokens[2:2 + n]
    asked = []
    pos = 2 + n
    for _ in range(m):
        asked.append((tokens[pos], tokens[pos + 1]))
        pos += 2
    return a, asked


# --- clause: candidate_spots :: (a: list[int]) -> dict[int, list[int]] ---
def candidate_spots(a):
    tally = {}
    for i in range(len(a)):
        item = a[i]
        if item > len(a):
            continue
        if item in tally:
            tally[item].append(i)
        else:
            tally[item] = [i]
    spots = {}
    for item in tally:
        if len(tally[item]) >= item:
            spots[item] = tally[item]
    return spots


# --- clause: answer_queries :: (spots: dict[int, list[int]], asked: list[tuple[int, int]]) -> list[int] ---
def answer_queries(spots, asked):
    out = []
    for low, high in asked:
        total = 0
        for item in spots:
            places = spots[item]
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
            if left - start == item:
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
