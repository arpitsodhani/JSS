# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        t = int(data[0])
        p = 1
        ans = []

        for _ in range(t):
            n = int(data[p])
            k = int(data[p + 1])
            s = data[p + 2]
            p += 3

            parity = [0] * k
            for i, ch in enumerate(s):
                if ch == '1':
                    parity[i % k] ^= 1

            ans.append("YES" if all(x == 0 for x in parity) else "NO")

        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
