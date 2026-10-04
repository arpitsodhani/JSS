import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        scores = list(map(int, data[idx:idx + n]))
        idx += n
        cases.append((n, scores))
    return cases


# --- clause: block_sizes :: (n: int, scores: list[int]) -> list[int] ---
def block_sizes(n, scores):
    sizes = []
    run = 1
    for i in range(1, n):
        if scores[i] != scores[i - 1]:
            sizes.append(run)
            run = 1
        else:
            run += 1
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
    if silver <= gold:
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
    for n, scores in read_input():
        gold, silver, bronze = award_medals(n, block_sizes(n, scores))
        out.append(str(gold) + " " + str(silver) + " " + str(bronze))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
