import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        pos += 3
        lists = [int(data[pos + i]) for i in range(m)]
        pos += m
        known = [int(data[pos + i]) for i in range(k)]
        pos += k
        cases.append((n, m, k, lists, known))
    return cases


# --- clause: solve_case :: (n: int, m: int, k: int, lists: list[int], known: list[int]) -> str ---
def solve_case(n, m, k, lists, known):
    missing = n - k
    if missing > 1:
        return "0" * m
    if missing == 0:
        return "1" * m
    seen = [False] * (n + 1)
    for question in known:
        seen[question] = True
    absent = 0
    for question in range(1, n + 1):
        if not seen[question]:
            absent = question
            break
    out = []
    for skipped in lists:
        if skipped == absent:
            out.append("1")
        else:
            out.append("0")
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(solve_case(case[0], case[1], case[2], case[3], case[4]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
