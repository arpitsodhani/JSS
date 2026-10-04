# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if len(tokens) == 0:
        return
    n = tokens[0]
    need = [0] + tokens[1:1 + n]
    unused = set(range(1, n + 1))
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    to = [1] * (n + 1)
    x[1] = 1
    y[1] = 1
    unused.remove(1)
    possible = True
    for i in range(2, n + 1):
        d = need[i]
        if d == 0:
            possible = False
            break
        preferred = d + 1
        if preferred in unused:
            x[i] = preferred
            y[i] = 1
            to[i] = 1
            unused.remove(preferred)
            continue
        if not unused:
            possible = False
            break
        col = min(unused)
        chosen_parent = 0
        chosen_row = 0
        j = 1
        while j < i and chosen_parent == 0:
            gap = d - abs(col - x[j])
            if gap >= 0:
                first = y[j] + gap
                second = y[j] - gap
                if 1 <= first <= n:
                    chosen_parent = j
                    chosen_row = first
                elif 1 <= second <= n:
                    chosen_parent = j
                    chosen_row = second
            j += 1
        if chosen_parent == 0:
            possible = False
            break
        x[i] = col
        y[i] = chosen_row
        to[i] = chosen_parent
        unused.remove(col)
    if not possible:
        sys.stdout.write("NO\n")
        return
    result = ["YES"]
    for i in range(1, n + 1):
        result.append("%d %d" % (x[i], y[i]))
    result.append(" ".join(map(str, to[1:])))
    sys.stdout.write("\n".join(result) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
