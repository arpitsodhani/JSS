# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_right

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, q = data[0], data[1]
        a = data[2:2 + n]
        queries = data[2 + n:2 + n + q]

        pref = []
        s = 0
        for x in a:
            s += x
            pref.append(s)

        total = pref[-1]
        damage = 0
        ans = []

        for k in queries:
            damage += k
            if damage >= total:
                ans.append(str(n))
                damage = 0
            else:
                fallen = bisect_right(pref, damage)
                ans.append(str(n - fallen))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
