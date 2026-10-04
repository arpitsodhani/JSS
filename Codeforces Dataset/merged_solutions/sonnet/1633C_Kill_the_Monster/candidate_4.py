import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    cursor = 1
    for _ in range(t):
        cases.append(tuple(numbers[cursor:cursor + 7]))
        cursor += 7
    return cases


# --- clause: can_win :: (hc: int, dc: int, hm: int, dm: int, k: int, a: int, w: int) -> bool ---
def can_win(hc, dc, hm, dm, k, a, w):
    spent = 0
    while spent <= k:
        power = dc + spent * a
        health = hc + (k - spent) * w
        hits = -(-hm // power)
        taken = -(-health // dm)
        if hits <= taken:
            return True
        spent += 1
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for hc, dc, hm, dm, k, a, w in read_input():
        out.append("YES" if can_win(hc, dc, hm, dm, k, a, w) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
