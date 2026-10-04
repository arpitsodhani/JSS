import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        m = raw[offset + 1]
        offset += 2
        cases.append((m, raw[offset:offset + n]))
        offset += n
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
    written = []
    for m, weights in read_input():
        plan = chain_plan(m, weights)
        if plan is None:
            written.append("-1")
        else:
            cost, chains = plan
            written.append(str(cost))
            for u, v in chains:
                written.append("%d %d" % (u, v))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
