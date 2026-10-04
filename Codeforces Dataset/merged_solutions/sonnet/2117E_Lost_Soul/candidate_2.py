import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases


# --- clause: best_prefix :: (a: list[int], b: list[int]) -> int ---
def best_prefix(a, b):
    n = len(a)
    tally = [[0, 0] for _ in range(n + 1)]
    for position in range(n, 0, -1):
        top = a[position - 1]
        bottom = b[position - 1]
        top_colour = position % 2
        bottom_colour = (position + 1) % 2
        if top == bottom:
            return position
        if tally[top][1 - top_colour] > 0 or tally[bottom][1 - bottom_colour] > 0:
            return position
        far_top = tally[top][top_colour]
        far_bottom = tally[bottom][bottom_colour]
        if position < n:
            later_top = a[position]
            later_bottom = b[position]
            later_top_colour = (position + 1) % 2
            later_bottom_colour = position % 2
            if later_top == top and later_top_colour == top_colour:
                far_top -= 1
            if later_bottom == top and later_bottom_colour == top_colour:
                far_top -= 1
            if later_top == bottom and later_top_colour == bottom_colour:
                far_bottom -= 1
            if later_bottom == bottom and later_bottom_colour == bottom_colour:
                far_bottom -= 1
        if far_top > 0 or far_bottom > 0:
            return position
        tally[top][top_colour] += 1
        tally[bottom][bottom_colour] += 1
    return 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(str(best_prefix(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
