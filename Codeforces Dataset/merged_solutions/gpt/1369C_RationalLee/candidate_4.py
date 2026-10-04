# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        out = []
        for _ in range(t):
            n = data[p]
            k = data[p + 1]
            p += 2
            a = data[p:p + n]
            p += n
            w = data[p:p + k]
            p += k

            a.sort()
            w.sort()

            ans = sum(a[n - k:])
            r = n - 1
            l = 0

            for x in w:
                if x == 1:
                    ans += a[r]
                    r -= 1
                else:
                    ans += a[l]
                    l += x - 1

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
