import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        scores = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append((n, scores))
    return cases


# --- clause: block_sizes :: (n: int, scores: list[int]) -> list[int] ---
def block_sizes(n, scores):
    sizes = []
    run = 1
    for i in range(1, n):
        if scores[i] == scores[i - 1]:
            run += 1
        else:
            sizes.append(run)
            run = 1
    sizes.append(run)
    return sizes


# --- clause: award_medals :: (n: int, sizes: list[int]) -> tuple[int, int, int] ---
def award_medals(n, sizes):
    limit = n // 2
    gold = sizes[0]
    index = 1
    silver = 0
    while index < len(sizes) and silver <= gold:
        silver += sizes[index]
        index += 1
    if not silver > gold:
        return 0, 0, 0
    bronze = 0
    while index < len(sizes) and gold + silver + bronze + sizes[index] <= limit:
        bronze += sizes[index]
        index += 1
    if bronze <= gold or gold + silver + bronze > limit:
        return 0, 0, 0
    return gold, silver, bronze


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        n, scores = case[0], case[1]
        gold, silver, bronze = award_medals(n, block_sizes(n, scores))
        out.append("%d %d %d" % (gold, silver, bronze))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
