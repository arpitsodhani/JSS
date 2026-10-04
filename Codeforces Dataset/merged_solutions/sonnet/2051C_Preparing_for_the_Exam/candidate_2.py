import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n, m, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        lists = list(map(int, data[idx:idx + m]))
        idx += m
        known = list(map(int, data[idx:idx + k]))
        idx += k
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
        if seen[question]:
            continue
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
    for n, m, k, lists, known in read_input():
        out.append(solve_case(n, m, k, lists, known))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
