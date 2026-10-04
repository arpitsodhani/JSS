import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), numbers[1].decode()


# --- clause: place_pieces :: (top: str, low: str) -> int ---
def place_pieces(top, low):
    n = len(top)
    blocked = []
    for i in range(n):
        blocked.append((1 if top[i] == "X" else 0) | (2 if low[i] == "X" else 0))
    table = [[-1] * 4 for _ in range(n + 1)]
    table[n][0] = 0
    for i in range(n - 1, -1, -1):
        for mask in range(4):
            if mask & blocked[i]:
                continue
            free = 3 & ~(mask | blocked[i])
            best = table[i + 1][0]
            if free == 3:
                for nxt in (1, 2):
                    here = table[i + 1][nxt]
                    if here >= 0 and here + 1 > best:
                        best = here + 1
            if free:
                here = table[i + 1][3]
                if here >= 0 and here + 1 > best:
                    best = here + 1
            table[i][mask] = best
    return table[0][0] if table[0][0] > 0 else 0


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % place_pieces(top, low))


if __name__ == "__main__":
    main()
