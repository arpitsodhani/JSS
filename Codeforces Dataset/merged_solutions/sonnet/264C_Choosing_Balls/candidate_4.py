import sys


# --- clause: read_input :: () -> tuple[list[int], list[int], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    q = numbers[1]
    values = numbers[2:2 + n]
    colours = numbers[2 + n:2 + 2 * n]
    cursor = 2 + 2 * n
    asked = []
    for i in range(q):
        asked.append((numbers[cursor + 2 * i], numbers[cursor + 1 + 2 * i]))
    return values, colours, asked


# --- clause: best_sequence :: (values: list[int], colours: list[int], a: int, b: int) -> int ---
def best_sequence(values, colours, a, b):
    n = len(values)
    none = -(1 << 62)
    best = [none] * (n + 2)
    ranked = [(none, -1), (none, -2)]
    answer = 0
    for i in range(n):
        value = values[i]
        colour = colours[i]
        outside = ranked[0][0] if ranked[0][1] != colour else ranked[1][0]
        if outside < 0:
            outside = 0
        here = outside + value * b
        if best[colour] > none:
            chain = best[colour] + value * a
            if chain > here:
                here = chain
        if here > best[colour]:
            best[colour] = here
        if here > answer:
            answer = here
        pair = (best[colour], colour)
        if pair[0] > ranked[0][0]:
            if ranked[0][1] != colour:
                ranked[1] = ranked[0]
            ranked[0] = pair
        elif ranked[0][1] != colour and pair[0] > ranked[1][0]:
            ranked[1] = pair
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
