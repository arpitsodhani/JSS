# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        if not data:
            return

        n = int(data[0])
        a = int(data[1])
        b = int(data[2])
        s = data[3]

        ans = 0
        prev = ""

        for ch in s:
            if ch == "*":
                prev = ""
                continue

            if prev == "A":
                if b > 0:
                    b -= 1
                    ans += 1
                    prev = "B"
                else:
                    prev = ""
            elif prev == "B":
                if a > 0:
                    a -= 1
                    ans += 1
                    prev = "A"
                else:
                    prev = ""
            else:
                if a >= b and a > 0:
                    a -= 1
                    ans += 1
                    prev = "A"
                elif b > 0:
                    b -= 1
                    ans += 1
                    prev = "B"
                else:
                    prev = ""

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
