import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    a = raw[2:2 + n]
    asked = []
    offset = 2 + n
    for _ in range(m):
        asked.append((raw[offset], raw[offset + 1]))
        offset += 2
    return a, asked


# --- clause: candidate_spots :: (a: list[int]) -> dict[int, list[int]] ---
def candidate_spots(a):
    tally = {}
    for i in range(0, len(a)):
        number = a[i]
        if number > len(a):
            continue
        if number in tally:
            tally[number].append(i)
        else:
            tally[number] = [i]
    spots = {}
    for number in tally:
        if len(tally[number]) >= number:
            spots[number] = tally[number]
    return spots


# --- clause: answer_queries :: (spots: dict[int, list[int]], asked: list[tuple[int, int]]) -> list[int] ---
def answer_queries(spots, asked):
    out = []
    for low, high in asked:
        total = 0
        for number in spots:
            places = spots[number]
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
            if left - start == number:
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
