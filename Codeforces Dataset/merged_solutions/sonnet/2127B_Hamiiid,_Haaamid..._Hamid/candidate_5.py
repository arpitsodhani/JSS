import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    reader = 1
    cases = []
    for _ in range(t):
        x = int(raw[reader + 1])
        s = raw[reader + 2].decode()
        reader += 3
        cases.append((x, s))
    return cases


# --- clause: escape_days :: (x: int, s: str) -> int ---
def escape_days(x, s):
    n = len(s)
    left = 0
    for i in range(x - 1, 0, -1):
        if s[i - 1] == "#":
            left = i
            break
    right = n + 1
    for i in range(x + 1, n + 1):
        if s[i - 1] == "#":
            right = i
            break
    plain_left = 1 + left
    plain_right = 1 + n + 1 - right
    top = 0
    if x > 1:
        value = x if x < plain_right else plain_right
        if value > top:
            top = value
    if x < n:
        value = plain_left if plain_left < n - x + 1 else n - x + 1
        if value > top:
            top = value
    if top == 0:
        top = plain_left if plain_left < plain_right else plain_right
    return top


# --- clause: main :: () -> None ---
def main():
    out = []
    for x, s in read_input():
        out.append(escape_days(x, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
