import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        q = int(data[pos + 1])
        pos += 2
        values = list(map(int, data[pos:pos + n]))
        pos += n
        queries = [int(token) for token in data[pos:pos + 2 * q]]
        pos += 2 * q
        cases.append((n, q, values, queries))
    return cases


# --- clause: answer_queries :: (n: int, q: int, values: list[int], queries: list[int]) -> list[str] ---
def answer_queries(n, q, values, queries):
    total = [0] * (n + 1)
    ones = [0] * (n + 1)
    running = 0
    singles = 0
    for i, value in enumerate(values):
        running += value
        if value == 1:
            singles += 1
        total[i + 1] = running
        ones[i + 1] = singles
    out = []
    for i in range(q):
        l = queries[2 * i]
        r = queries[2 * i + 1]
        width = r - l + 1
        if width < 2:
            out.append("NO")
            continue
        need = width + ones[r] - ones[l - 1]
        if total[r] - total[l - 1] >= need:
            out.append("YES")
        else:
            out.append("NO")
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, q, values, queries in read_input():
        out.extend(answer_queries(n, q, values, queries))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
