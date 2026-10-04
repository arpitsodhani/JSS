import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    q = int(data[2])
    queries = []
    for step in range(q):
        i = int(data[3 + 2 * step])
        j = int(data[4 + 2 * step])
        queries.append((i, j))
    return n, m, q, queries


# --- clause: classify_cell :: (i: int, j: int) -> tuple[int, int, int] ---
def classify_cell(i, j):
    if i % 2 == 1:
        return (i + 1) // 2, (j + 1) // 2, 0
    return i // 2, j // 2, 1


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
                best = -1
                node = n + 1 - r
                while node > 0:
                    if high_col[node] > best:
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
                best = infinity
                node = r
                while node > 0:
                    if low_col[node] < best:
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
        if broken:
            answers.append("NO")
        else:
            answers.append("YES")
    return answers


# --- clause: main :: () -> None ---
def main():
    n, m, q, queries = read_input()
    answers = answer_queries(n, m, q, queries)
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
