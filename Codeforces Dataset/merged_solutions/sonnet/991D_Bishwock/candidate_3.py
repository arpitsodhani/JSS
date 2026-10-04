import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[0].decode(), fields[1].decode()


# --- clause: place_pieces :: (top: str, low: str) -> int ---
def place_pieces(top, low):
    n = len(top)
    none = -1
    champion = [none] * 4
    champion[0] = 0
    for i in range(n):
        blocked = (1 if top[i] == "X" else 0) | (2 if low[i] == "X" else 0)
        fresh = [none] * 4
        for state in range(4):
            entry = champion[state]
            if entry == none or state & blocked:
                continue
            free = 3 & ~(state | blocked)
            if entry > fresh[0]:
                fresh[0] = entry
            if free == 3:
                if entry + 1 > fresh[1]:
                    fresh[1] = entry + 1
                if entry + 1 > fresh[2]:
                    fresh[2] = entry + 1
            if free and entry + 1 > fresh[3]:
                fresh[3] = entry + 1
        champion = fresh
    return champion[0] if champion[0] > 0 else 0


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % place_pieces(top, low))


if __name__ == "__main__":
    main()
