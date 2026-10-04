import sys


# --- clause: read_input :: () -> tuple[list[int], list[int], list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    q = raw[1]
    values = raw[2:2 + n]
    colours = raw[2 + n:2 + 2 * n]
    reader = 2 + 2 * n
    asked = []
    for i in range(q):
        asked.append((raw[reader + 2 * i], raw[reader + 1 + 2 * i]))
    return values, colours, asked


# --- clause: best_sequence :: (values: list[int], colours: list[int], a: int, b: int) -> int ---
def best_sequence(values, colours, a, b):
    n = len(values)
    none = -(1 << 62)
    best = [none] * (n + 2)
    top = none
    two = none
    top_colour = -1
    answer = 0
    for i in range(n):
        value = values[i]
        colour = colours[i]
        other = two if top_colour == colour else top
        base = other if other > 0 else 0
        here = base + value * b
        if best[colour] > none:
            chain = best[colour] + value * a
            if chain > here:
                here = chain
        if here > best[colour]:
            best[colour] = here
        if here > answer:
            answer = here
        if best[colour] > top:
            if top_colour != colour:
                two = top
            top = best[colour]
            top_colour = colour
        elif top_colour != colour and best[colour] > two:
            two = best[colour]
    return answer


# --- clause: main :: () -> None ---
def main():
    values, colours, asked = read_input()
    out = []
    for a, b in asked:
        out.append(best_sequence(values, colours, a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
