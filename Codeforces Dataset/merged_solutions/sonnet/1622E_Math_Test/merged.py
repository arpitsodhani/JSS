import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        wanted = [int(v) for v in data[pos:pos + n]]
        pos += n
        sheets = [data[pos + i].decode() for i in range(n)]
        pos += n
        cases.append((m, wanted, sheets))
    return cases

# Clause question_groups [Confidence: 1.00]
def question_groups(n, m, sheets):
    marks = [0] * m
    for i in range(n):
        band = sheets[i]
        bit = 1 << i
        for j in range(m):
            if band[j] == "1":
                marks[j] |= bit
    return marks

# Clause best_permutation [Confidence: 1.00]
def best_permutation(n, m, wanted, marks):
    groups = {}
    for j in range(m):
        if marks[j] in groups:
            groups[marks[j]].append(j)
        else:
            groups[marks[j]] = [j]
    keys = list(groups)
    best_value = None
    best_order = None
    for mask in range(1 << n):
        weight = []
        for key in keys:
            here = 0
            for i in range(n):
                if (key >> i) & 1:
                    here += 1 if (mask >> i) & 1 else -1
            weight.append(here)
        ranked = sorted(range(len(keys)), key=lambda idx: weight[idx])
        value = 0
        for i in range(n):
            value -= wanted[i] if (mask >> i) & 1 else -wanted[i]
        points = 1
        for idx in ranked:
            for _ in groups[keys[idx]]:
                value += weight[idx] * points
                points += 1
        if best_value is None or value > best_value:
            best_value = value
            best_order = ranked
    scores = [0] * m
    points = 1
    for idx in best_order:
        for j in groups[keys[idx]]:
            scores[j] = points
            points += 1
    return scores

# Clause main [Confidence: 1.00]
def main():
    out = []
    for m, wanted, sheets in read_input():
        n = len(wanted)
        marks = question_groups(n, m, sheets)
        out.append(" ".join(map(str, best_permutation(n, m, wanted, marks))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

