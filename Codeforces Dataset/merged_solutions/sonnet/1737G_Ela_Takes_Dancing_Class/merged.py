# Clause setup_environment [Confidence: 0.40]
import sys

def main():
    items = sys.stdin.buffer.read().split()
    cursor = 0
    n = int(items[cursor])
    cursor += 1
    m = int(items[cursor])
    cursor += 1
    q = int(items[cursor])
    cursor += 1
    original = []
    for _ in range(n):
        original.append(int(items[cursor]))
        cursor += 1
    mask = items[cursor]
    cursor += 1
    movable_indexes = [i for i, b in enumerate(mask) if b == 49]
    result = []


# Clause solve_logic [Confidence: 0.40]
    for _ in range(q):
        d = int(tokens[p])
        who = int(tokens[p + 1]) - 1
        p += 2

        pos = base[:]
        can = [c == "1" for c in flags]

        for _ in range(m):
            chosen = -1
            chosen_x = None
            for i, x in enumerate(pos):
                if can[i] and (chosen_x is None or x < chosen_x):
                    chosen = i
                    chosen_x = x

            if chosen < 0:
                break

            wall = None
            start = pos[chosen]
            for i, x in enumerate(pos):
                if i != chosen and x > start and (wall is None or x < wall):
                    wall = x

            if wall is None:
                pos[chosen] = start + d
            else:
                moved = start + d
                pos[chosen] = moved if moved < wall else wall - 1
            can[chosen] = False

        ans.append(str(pos[who]))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()


