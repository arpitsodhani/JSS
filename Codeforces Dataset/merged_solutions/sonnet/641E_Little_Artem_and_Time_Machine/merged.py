import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    queries = []
    for i in range(n):
        queries.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return queries

# Clause group_by_value [Confidence: 1.00]
def group_by_value(queries):
    groups = {}
    for spot in range(len(queries)):
        kind, moment, element = queries[spot]
        if element not in groups:
            groups[element] = []
        groups[element].append((spot, kind, moment))
    return groups

# Clause answer_group [Confidence: 1.00]
def answer_group(rows, answers):
    moments = sorted(set(row[2] for row in rows))
    place = {}
    for i in range(len(moments)):
        place[moments[i]] = i + 1
    tree = [0] * (len(moments) + 1)
    for spot, kind, moment in rows:
        index = place[moment]
        if kind == 3:
            summed = 0
            walk = index
            while walk > 0:
                summed += tree[walk]
                walk -= walk & (-walk)
            answers[spot] = summed
        else:
            delta = 1 if kind == 1 else -1
            walk = index
            while walk <= len(moments):
                tree[walk] += delta
                walk += walk & (-walk)

# Clause main [Confidence: 1.00]
def main():
    queries = read_input()
    answers = {}
    groups = group_by_value(queries)
    for element in groups:
        answer_group(groups[element], answers)
    out = []
    for spot in sorted(answers):
        out.append(answers[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

