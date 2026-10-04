import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: can_eat :: (a: list[int]) -> bool ---
def can_eat(a):
    if len(a) == 1:
        return a[0] == 1
    top = 0
    second = 0
    for value in a:
        if value > top:
            second = top
            top = value
        elif value > second:
            second = value
    return top - second <= 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_eat(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
