import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    w = int(data[1])
    h = int(data[2])
    dancers = []
    pos = 3
    for _ in range(n):
        dancers.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2])))
        pos += 3
    return n, w, h, dancers

# Clause group_dancers [Confidence: 0.80]
def group_dancers(n, dancers):
    groups = {}
    for i in range(n):
        g, p, t = dancers[i]
        key = p - t
        if key in groups:
            groups[key].append(i)
        else:
            groups[key] = [i]
    return groups

# Clause final_spots [Confidence: 1.00]
def final_spots(w, h, dancers, groups):
    answer = [None] * len(dancers)
    for members in groups.values():
        starts = []
        ends = []
        for i in members:
            g, p, t = dancers[i]
            if g == 2:
                starts.append((0, p, i))
                ends.append((w, p))
            else:
                starts.append((p, 0, i))
                ends.append((p, h))
        starts.sort(key=lambda item: (item[0], -item[1]))
        ends.sort(key=lambda item: (item[0], -item[1]))
        for spot, target in zip(starts, ends):
            answer[spot[2]] = "%d %d" % (target[0], target[1])
    return answer

# Clause main [Confidence: 1.00]
def main():
    n, w, h, dancers = read_input()
    groups = group_dancers(n, dancers)
    sys.stdout.write("\n".join(final_spots(w, h, dancers, groups)) + "\n")


if __name__ == "__main__":
    main()

