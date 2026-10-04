import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: can_eat :: (a: list[int]) -> bool ---
def can_eat(a):
    if len(a) == 1:
        return a[0] == 1
    top = 0
    second = 0
    for element in a:
        if element > top:
            second = top
            top = element
        elif element > second:
            second = element
    return top - second <= 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_eat(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
