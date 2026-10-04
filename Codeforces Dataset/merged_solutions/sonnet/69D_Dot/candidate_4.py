# CLAUSE: setup_environment
import sys

sys.setrecursionlimit(1000000)


# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    if len(tokens) < 4:
        return

    x = int(tokens[0])
    y = int(tokens[1])
    n = int(tokens[2])
    d = int(tokens[3])
    shifts = tuple((int(tokens[i]), int(tokens[i + 1])) for i in range(4, 4 + 2 * n, 2))
    max_dist = d * d
    cache = {}
    route = set()

    def legal(a, b):
        return a * a + b * b <= max_dist

    def dfs(state):
        if state in cache:
            return cache[state]
        if state in route:
            return False

        a, b, flags, turn = state
        route.add(state)

        i = 0
        while i < len(shifts):
            da, db = shifts[i]
            na = a + da
            nb = b + db
            if legal(na, nb):
                child = (na, nb, flags, turn ^ 1)
                if not dfs(child):
                    route.remove(state)
                    cache[state] = True
                    return True
            i += 1

        bit = 1 << turn
        if flags & bit == 0 and legal(b, a):
            child = (b, a, flags | bit, turn ^ 1)
            if not dfs(child):
                route.remove(state)
                cache[state] = True
                return True

        route.remove(state)
        cache[state] = False
        return False

    result = dfs((x, y, 0, 0))
    sys.stdout.write(("Anton" if result else "Dasha") + "\n")


# CLAUSE: finish_program
if __name__ == "__main__":
    main()
