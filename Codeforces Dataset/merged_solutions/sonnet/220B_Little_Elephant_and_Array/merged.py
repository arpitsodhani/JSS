import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    a = data[2:2 + n]
    asked = []
    pos = 2 + n
    for _ in range(m):
        asked.append((data[pos], data[pos + 1]))
        pos += 2
    return a, asked

# Clause candidate_spots [Confidence: 1.00]
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

# Clause answer_queries [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    a, asked = read_input()
    spots = candidate_spots(a)
    sys.stdout.write("\n".join(map(str, answer_queries(spots, asked))) + "\n")


if __name__ == "__main__":
    main()

