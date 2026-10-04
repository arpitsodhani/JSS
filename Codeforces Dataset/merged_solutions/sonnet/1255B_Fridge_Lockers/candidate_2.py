import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        m = tokens[pos + 1]
        pos += 2
        cases.append((m, tokens[pos:pos + n]))
        pos += n
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
    lines = []
    for m, weights in read_input():
        plan = chain_plan(m, weights)
        if plan is None:
            lines.append("-1")
        else:
            cost, chains = plan
            lines.append(str(cost))
            for u, v in chains:
                lines.append("%d %d" % (u, v))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
