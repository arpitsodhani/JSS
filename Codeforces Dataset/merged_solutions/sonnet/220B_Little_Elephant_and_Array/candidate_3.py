import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    a = fields[2:2 + n]
    asked = []
    cursor = 2 + n
    for _ in range(m):
        asked.append((fields[cursor], fields[cursor + 1]))
        cursor += 2
    return a, asked


# --- clause: candidate_spots :: (a: list[int]) -> dict[int, list[int]] ---
def candidate_spots(a):
    tally = {}
    for i in range(len(a)):
        element = a[i]
        if element > len(a):
            continue
        if element in tally:
            tally[element].append(i)
        else:
            tally[element] = [i]
    spots = {}
    for element in tally:
        if len(tally[element]) >= element:
            spots[element] = tally[element]
    return spots


# --- clause: answer_queries :: (spots: dict[int, list[int]], asked: list[tuple[int, int]]) -> list[int] ---
def answer_queries(spots, asked):
    out = []
    for low, high in asked:
        total = 0
        for element in spots:
            places = spots[element]
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
            if left - start == element:
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
