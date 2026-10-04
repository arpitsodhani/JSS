# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            q = data[idx + 2]
            idx += 3

            a = data[idx:idx + n]
            idx += n

            b = data[idx:idx + m]
            idx += m

            seen = set()
            p = 0
            ok = True

            for x in b:
                if x in seen:
                    continue
                if p < n and x == a[p]:
                    seen.add(x)
                    p += 1
                else:
                    ok = False
                    break

            out.append("YA" if ok else "TIDAK")

            idx += 2 * q

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
