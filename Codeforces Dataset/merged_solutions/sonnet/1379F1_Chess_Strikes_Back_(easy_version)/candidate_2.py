import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    queries = []
    idx = 3
    for _ in range(q):
        i, j = int(data[idx]), int(data[idx + 1])
        idx += 2
        queries.append((i, j))
    return n, m, q, queries


# --- clause: classify_cell :: (i: int, j: int) -> tuple[int, int, int] ---
def classify_cell(i, j):
    if i % 2 == 0:
        return i // 2, j // 2, 1
    return (i + 1) // 2, (j + 1) // 2, 0


# --- clause: answer_queries :: (n: int, m: int, q: int, queries: list[tuple[int, int]]) -> list[str] ---
def answer_queries(n, m, q, queries):
    infinity = 1 << 60
    low_col = [infinity] * (n + 1)
    high_col = [-1] * (n + 1)
    answers = []
    broken = False
    for i, j in queries:
        if not broken:
            r, c, forced = classify_cell(i, j)
            if forced == 0:
                node = n + 1 - r
                best = -1
                while node > 0:
                    if best < high_col[node]:
                        best = high_col[node]
                    node -= node & -node
                if best >= c:
                    broken = True
                else:
                    node = r
                    while node <= n:
                        if c < low_col[node]:
                            low_col[node] = c
                        node += node & -node
            else:
                node = r
                best = infinity
                while node > 0:
                    if best > low_col[node]:
                        best = low_col[node]
                    node -= node & -node
                if best <= c:
                    broken = True
                else:
                    node = n + 1 - r
                    while node <= n:
                        if c > high_col[node]:
                            high_col[node] = c
                        node += node & -node
        answers.append("NO" if broken else "YES")
    return answers


# --- clause: main :: () -> None ---
def main():
    n, m, q, queries = read_input()
    sys.stdout.write("%s\n" % "\n".join(answer_queries(n, m, q, queries)))


if __name__ == "__main__":
    main()
