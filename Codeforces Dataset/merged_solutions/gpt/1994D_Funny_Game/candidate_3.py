# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            pos = list(range(n))
            ans = []

            for m in range(n - 1, 0, -1):
                seen = [-1] * m
                for k, v in enumerate(pos):
                    r = a[v] % m
                    if seen[r] != -1:
                        ans.append((v + 1, seen[r] + 1))
                        pos.pop(k)
                        break
                    seen[r] = v

            out.append("YES")
            for u, v in reversed(ans):
                out.append(f"{u} {v}")

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
