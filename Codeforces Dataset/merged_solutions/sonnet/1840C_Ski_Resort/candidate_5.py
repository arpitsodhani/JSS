import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        k = raw[offset + 1]
        q = raw[offset + 2]
        offset += 3
        cases.append((k, q, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: count_vacations :: (k: int, q: int, a: list[int]) -> int ---
def count_vacations(k, q, a):
    running = 0
    run = 0
    for value in a + [q + 1]:
        if value <= q:
            run += 1
            continue
        if run >= k:
            spare = run - k + 1
            running += spare * (spare + 1) // 2
        run = 0
    return running


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, q, a in read_input():
        out.append(count_vacations(k, q, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
