import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    offset = 1
    papers = []
    for _ in range(n * (n - 1) // 2):
        k = fields[offset]
        offset += 1
        papers.append(fields[offset:offset + k])
        offset += k
    return papers


# --- clause: group_elements :: (papers: list[list[int]]) -> list[list[int]] ---
def group_elements(papers):
    where = {}
    for position in range(len(papers)):
        for value in papers[position]:
            if value in where:
                where[value].append(position)
            else:
                where[value] = [position]
    families = {}
    for value in where:
        key = tuple(where[value])
        if key in families:
            families[key].append(value)
        else:
            families[key] = [value]
    return [sorted(group) for group in families.values()]


# --- clause: main :: () -> None ---
def main():
    out = []
    for group in group_elements(read_input()):
        out.append(" ".join(map(str, [len(group)] + group)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
