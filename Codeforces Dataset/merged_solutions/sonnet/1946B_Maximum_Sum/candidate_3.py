import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        k = fields[cursor + 1]
        cursor += 2
        cases.append((k, fields[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: best_piece :: (a: list[int]) -> int ---
def best_piece(a):
    best = 0
    running = 0
    lowest = 0
    for value in a:
        running += value
        if running - lowest > best:
            best = running - lowest
        if running < lowest:
            lowest = running
    return best


# --- clause: grown_sum :: (k: int, a: list[int]) -> int ---
def grown_sum(k, a):
    mod = 1000000007
    piece = best_piece(a)
    return (sum(a) + piece * (pow(2, k, mod) - 1)) % mod


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(grown_sum(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
