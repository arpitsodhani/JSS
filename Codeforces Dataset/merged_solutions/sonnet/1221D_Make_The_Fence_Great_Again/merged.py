import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    q = data[0]
    pos = 1
    cases = []
    for _ in range(q):
        n = data[pos]
        pos += 1
        boards = [(data[pos + 2 * i], data[pos + 2 * i + 1]) for i in range(n)]
        pos += 2 * n
        cases.append(boards)
    return cases

# Clause least_rubles [Confidence: 1.00]
def least_rubles(boards):
    big = float("inf")
    best = [0, boards[0][1], 2 * boards[0][1]]
    for i in range(1, len(boards)):
        height, price = boards[i]
        before = boards[i - 1][0]
        step = [big, big, big]
        for add in range(3):
            for prev in range(3):
                if height + add == before + prev:
                    continue
                element = best[prev] + add * price
                if element < step[add]:
                    step[add] = element
        best = step
    return min(best)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for boards in read_input():
        out.append(least_rubles(boards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

