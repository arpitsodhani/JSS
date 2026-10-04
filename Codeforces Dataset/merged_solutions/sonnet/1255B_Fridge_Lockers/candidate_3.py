import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        m = fields[cursor + 1]
        cursor += 2
        cases.append((m, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: chain_plan :: (m: int, weights: list[int]) -> tuple[int, list[tuple[int, int]]] | None ---
def chain_plan(m, weights):
    n = len(weights)
    if n == 2 or m != n:
        return None
    chains = []
    for i in range(n):
        chains.append((i + 1, (i + 1) % n + 1))
    return 2 * sum(weights), chains


# --- clause: main :: () -> None ---
def main():
    collected = []
    for m, weights in read_input():
        plan = chain_plan(m, weights)
        if plan is None:
            collected.append("-1")
        else:
            cost, chains = plan
            collected.append(str(cost))
            for u, v in chains:
                collected.append("%d %d" % (u, v))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
