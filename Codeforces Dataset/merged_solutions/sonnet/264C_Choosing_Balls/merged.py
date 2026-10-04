import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    values = data[2:2 + n]
    colours = data[2 + n:2 + 2 * n]
    pos = 2 + 2 * n
    asked = []
    for i in range(q):
        asked.append((data[pos + 2 * i], data[pos + 1 + 2 * i]))
    return values, colours, asked

# Clause best_sequence [Confidence: 1.00]
def best_sequence(values, colours, a, b):
    n = len(values)
    none = -(1 << 62)
    best = [none] * (n + 2)
    top = none
    follow = none
    top_colour = -1
    answer = 0
    for i in range(n):
        value = values[i]
        colour = colours[i]
        other = follow if top_colour == colour else top
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
                follow = top
            top = best[colour]
            top_colour = colour
        elif top_colour != colour and best[colour] > follow:
            follow = best[colour]
    return answer

# Clause main [Confidence: 1.00]
def main():
    values, colours, asked = read_input()
    out = []
    for a, b in asked:
        out.append(best_sequence(values, colours, a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

