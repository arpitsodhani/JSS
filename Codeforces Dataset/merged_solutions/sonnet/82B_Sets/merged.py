import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    papers = []
    for _ in range(n * (n - 1) // 2):
        k = data[pos]
        pos += 1
        papers.append(data[pos:pos + k])
        pos += k
    return papers

# Clause group_elements [Confidence: 1.00]
def group_elements(papers):
    where = {}
    for index in range(len(papers)):
        for value in papers[index]:
            if value in where:
                where[value].append(index)
            else:
                where[value] = [index]
    families = {}
    for value in where:
        key = tuple(where[value])
        if key in families:
            families[key].append(value)
        else:
            families[key] = [value]
    return [sorted(group) for group in families.values()]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for group in group_elements(read_input()):
        out.append(" ".join(map(str, [len(group)] + group)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

