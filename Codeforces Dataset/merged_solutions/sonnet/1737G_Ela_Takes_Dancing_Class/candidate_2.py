# CLAUSE: setup_environment
import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    p = 0
    n = int(tokens[p])
    m = int(tokens[p + 1])
    q = int(tokens[p + 2])
    p += 3
    base = list(map(int, tokens[p:p + n]))
    p += n
    flags = tokens[p].decode()
    p += 1
    ans = []

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
