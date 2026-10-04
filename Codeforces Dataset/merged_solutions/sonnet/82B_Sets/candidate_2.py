import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    at = 1
    papers = []
    for _ in range(n * (n - 1) // 2):
        k = tokens[at]
        at += 1
        papers.append(tokens[at:at + k])
        at += k
    return papers


# --- clause: group_elements :: (papers: list[list[int]]) -> list[list[int]] ---
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


# --- clause: main :: () -> None ---
def main():
    out = []
    for group in group_elements(read_input()):
        out.append(" ".join(map(str, [len(group)] + group)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
