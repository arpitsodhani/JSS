import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: can_eat :: (a: list[int]) -> bool ---
def can_eat(a):
    if len(a) == 1:
        return a[0] == 1
    top = 0
    second = 0
    for number in a:
        if number > top:
            second = top
            top = number
        elif number > second:
            second = number
    return top - second <= 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_eat(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
