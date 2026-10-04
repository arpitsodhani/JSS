import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[0].decode(), raw[1].decode()


# --- clause: place_pieces :: (top: str, low: str) -> int ---
def place_pieces(top, low):
    n = len(top)
    none = -1
    best = [none] * 4
    best[0] = 0
    for i in range(n):
        blocked = (1 if top[i] == "X" else 0) | (2 if low[i] == "X" else 0)
        fresh = [none] * 4
        for state in range(4):
            item = best[state]
            if item == none or state & blocked:
                continue
            free = 3 & ~(state | blocked)
            if item > fresh[0]:
                fresh[0] = item
            if free == 3:
                if item + 1 > fresh[1]:
                    fresh[1] = item + 1
                if item + 1 > fresh[2]:
                    fresh[2] = item + 1
            if free and item + 1 > fresh[3]:
                fresh[3] = item + 1
        best = fresh
    return best[0] if best[0] > 0 else 0


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % place_pieces(top, low))


if __name__ == "__main__":
    main()
