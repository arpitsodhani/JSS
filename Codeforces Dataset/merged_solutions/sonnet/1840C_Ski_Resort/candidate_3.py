import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        k = fields[cursor + 1]
        q = fields[cursor + 2]
        cursor += 3
        cases.append((k, q, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: count_vacations :: (k: int, q: int, a: list[int]) -> int ---
def count_vacations(k, q, a):
    tally = 0
    run = 0
    for value in a + [q + 1]:
        if value <= q:
            run += 1
            continue
        if run >= k:
            spare = run - k + 1
            tally += spare * (spare + 1) // 2
        run = 0
    return tally


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, q, a in read_input():
        out.append(count_vacations(k, q, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
