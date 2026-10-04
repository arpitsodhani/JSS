import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        pos += 3
        lists = [int(token) for token in data[pos:pos + m]]
        pos += m
        known = [int(token) for token in data[pos:pos + k]]
        pos += k
        cases.append((n, m, k, lists, known))
    return cases


# --- clause: solve_case :: (n: int, m: int, k: int, lists: list[int], known: list[int]) -> str ---
def solve_case(n, m, k, lists, known):
    missing = n - k
    if missing == 0:
        return "1" * m
    if missing > 1:
        return "0" * m
    seen = [False] * (n + 1)
    for question in known:
        seen[question] = True
    absent = 0
    for question in range(1, n + 1):
        if not seen[question]:
            absent = question
            break
    marks = []
    index = 0
    while index < m:
        if lists[index] == absent:
            marks.append("1")
        else:
            marks.append("0")
        index += 1
    return "".join(marks)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, k, lists, known in read_input():
        out.append(solve_case(n, m, k, lists, known))
    print("\n".join(out))


if __name__ == "__main__":
    main()
