import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return tokens[0].decode(), tokens[1].decode()


# --- clause: place_pieces :: (top: str, low: str) -> int ---
def place_pieces(top, low):
    n = len(top)
    none = -1
    finest = [none] * 4
    finest[0] = 0
    for i in range(n):
        blocked = (1 if top[i] == "X" else 0) | (2 if low[i] == "X" else 0)
        fresh = [none] * 4
        for state in range(4):
            value = finest[state]
            if value == none or state & blocked:
                continue
            free = 3 & ~(state | blocked)
            if value > fresh[0]:
                fresh[0] = value
            if free == 3:
                if value + 1 > fresh[1]:
                    fresh[1] = value + 1
                if value + 1 > fresh[2]:
                    fresh[2] = value + 1
            if free and value + 1 > fresh[3]:
                fresh[3] = value + 1
        finest = fresh
    return finest[0] if finest[0] > 0 else 0


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % place_pieces(top, low))


if __name__ == "__main__":
    main()
