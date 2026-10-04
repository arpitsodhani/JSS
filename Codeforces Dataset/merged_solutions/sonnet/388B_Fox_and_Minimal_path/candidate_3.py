# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def one_bits(number):
    result = []
    place = 0
    while number > 0:
        if number % 2 == 1:
            result.append(place)
        number //= 2
        place += 1
    return result

def solve(k):
    bits = one_bits(k)
    if k == 1:
        return "2\nNY\nYN"

    top = max(bits)
    n = top * 2 + 2
    edges = set()

    layers = []
    for i in range(top + 1):
        if i == 0:
            layers.append((0,))
        else:
            layers.append((2 + (i - 1) * 2, 3 + (i - 1) * 2))

    for i in range(top):
        for u in layers[i]:
            for v in layers[i + 1]:
                if u < v:
                    edges.add((u, v))
                else:
                    edges.add((v, u))

    for bit in bits:
        if bit == 0:
            edges.add((0, 1))
        else:
            a = layers[bit][0]
            if a < 1:
                edges.add((a, 1))
            else:
                edges.add((1, a))

    rows = []
    for i in range(n):
        line = []
        for j in range(n):
            a, b = (i, j) if i < j else (j, i)
            line.append("Y" if (a, b) in edges else "N")
        rows.append("".join(line))

    return "\n".join([str(n)] + rows)

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().strip()
    if data:
        sys.stdout.write(solve(int(data)))

if __name__ == "__main__":
    main()
