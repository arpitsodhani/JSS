import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    offset = 1
    for _ in range(t):
        cases.append(tuple(fields[offset:offset + 7]))
        offset += 7
    return cases


# --- clause: can_win :: (hc: int, dc: int, hm: int, dm: int, k: int, a: int, w: int) -> bool ---
def can_win(hc, dc, hm, dm, k, a, w):
    for spent in range(k + 1):
        power = dc + spent * a
        health = hc + (k - spent) * w
        hits = (hm + power - 1) // power
        taken = (health + dm - 1) // dm
        if hits <= taken:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for hc, dc, hm, dm, k, a, w in read_input():
        pieces.append("YES" if can_win(hc, dc, hm, dm, k, a, w) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
