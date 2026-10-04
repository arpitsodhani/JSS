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
            k, n, m = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            a = data[idx:idx + n]
            idx += n
            b = data[idx:idx + m]
            idx += m

            i = j = 0
            ans = []

            while i < n or j < m:
                if i < n and a[i] == 0:
                    ans.append(0)
                    k += 1
                    i += 1
                elif j < m and b[j] == 0:
                    ans.append(0)
                    k += 1
                    j += 1
                elif i < n and a[i] <= k:
                    ans.append(a[i])
                    i += 1
                elif j < m and b[j] <= k:
                    ans.append(b[j])
                    j += 1
                else:
                    ans = None
                    break

            if ans is None:
                out.append("-1")
            else:
                out.append(" ".join(map(str, ans)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
