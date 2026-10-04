# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def add_interval(starts, ends, lo, hi, chance):
    if chance < 100:
        keep = (100 - chance) / 100.0
        starts.append((lo, keep))
        ends.append((hi, keep))

def main():
    tokens = sys.stdin.buffer.read().split()
    index = 0
    n = int(tokens[index])
    m = int(tokens[index + 1])
    index += 2

    starts = []
    ends = []

    for _ in range(n):
        a = int(tokens[index])
        h = int(tokens[index + 1])
        l = int(tokens[index + 2])
        r = int(tokens[index + 3])
        index += 4
        add_interval(starts, ends, a - h, a, l)
        add_interval(starts, ends, a + 1, a + h + 1, r)

    mushrooms = []
    for _ in range(m):
        mushrooms.append((int(tokens[index]), int(tokens[index + 1])))
        index += 2

    starts.sort(key=lambda item: item[0])
    ends.sort(key=lambda item: item[0])
    mushrooms.sort(key=lambda item: item[0])

    si = 0
    ei = 0
    active = 1.0
    result = 0.0

    for coordinate, value in mushrooms:
        while si < len(starts):
            where, keep = starts[si]
            if where > coordinate:
                break
            active *= keep
            si += 1

        while ei < len(ends):
            where, keep = ends[ei]
            if where > coordinate:
                break
            active /= keep
            ei += 1

        result += value * active

    print("%.10f" % result)

# CLAUSE: finish_program
main()
