import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    dances = []
    pos = 2
    for _ in range(m):
        dances.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return n, m, dances

# --- clause: assign_colors :: (n: int, dances: list[tuple[int, int, int]]) -> list[int] ---
def assign_colors(n, dances):
    color = [0] * (n + 1)
    for a, b, c in dances:
        known = color[a] or color[b] or color[c]
        free = []
        for shade in (1, 2, 3):
            if shade != known:
                free.append(shade)
        for dancer in (a, b, c):
            if color[dancer] == 0:
                color[dancer] = free.pop()
    return color[1:]

# --- clause: main :: () -> None ---
def main():
    n, m, dances = read_input()
    sys.stdout.write(" ".join(map(str, assign_colors(n, dances))) + "\n")


if __name__ == "__main__":
    main()
