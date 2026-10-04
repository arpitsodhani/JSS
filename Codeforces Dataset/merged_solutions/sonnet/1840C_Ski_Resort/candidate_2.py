import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        k = tokens[pos + 1]
        q = tokens[pos + 2]
        pos += 3
        cases.append((k, q, tokens[pos:pos + n]))
        pos += n
    return cases


# --- clause: count_vacations :: (k: int, q: int, a: list[int]) -> int ---
def count_vacations(k, q, a):
    amount = 0
    run = 0
    for value in a + [q + 1]:
        if value <= q:
            run += 1
            continue
        if run >= k:
            spare = run - k + 1
            amount += spare * (spare + 1) // 2
        run = 0
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, q, a in read_input():
        out.append(count_vacations(k, q, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
