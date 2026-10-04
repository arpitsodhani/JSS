# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        h, n = data[0], data[1]
        d = data[2:2 + n]

        pref = []
        s = 0
        mn = 10**30

        for x in d:
            s += x
            pref.append(s)
            if s < mn:
                mn = s

        for i, p in enumerate(pref, 1):
            if h + p <= 0:
                print(i)
                return

        if s >= 0:
            print(-1)
            return

        damage = -s
        rounds = max(0, (h + mn + damage - 1) // damage)

        hp_start = h + rounds * s
        for i, p in enumerate(pref, 1):
            if hp_start + p <= 0:
                print(rounds * n + i)
                return

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
