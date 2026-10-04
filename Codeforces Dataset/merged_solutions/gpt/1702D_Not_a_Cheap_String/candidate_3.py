# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        t = int(data[0])
        idx = 1
        ans = []

        for _ in range(t):
            s = data[idx]
            p = int(data[idx + 1])
            idx += 2

            total = sum(ord(c) - 96 for c in s)
            remove = [0] * 26

            for v in range(25, -1, -1):
                if total <= p:
                    break
                cnt = s.count(chr(97 + v))
                take = min(cnt, (total - p + v) // (v + 1))
                remove[v] = take
                total -= take * (v + 1)

            res = []
            for c in s:
                v = ord(c) - 97
                if remove[v]:
                    remove[v] -= 1
                else:
                    res.append(c)

            ans.append(''.join(res))

        sys.stdout.write('\n'.join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
