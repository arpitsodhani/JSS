# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        input = sys.stdin.readline
        n, k = map(int, input().split())
        s = list(input().strip())

        layers = []
        total = 0

        while True:
            cur = []
            i = 0
            while i < n - 1:
                if s[i] == 'R' and s[i + 1] == 'L':
                    cur.append(i + 1)
                    s[i], s[i + 1] = s[i + 1], s[i]
                    i += 2
                else:
                    i += 1
            if not cur:
                break
            layers.append(cur)
            total += len(cur)

        if k < len(layers) or k > total:
            print(-1)
            return

        extra = k - len(layers)
        ans = []

        for cur in layers:
            idx = 0
            while extra > 0 and idx < len(cur) - 1:
                ans.append([cur[idx]])
                idx += 1
                extra -= 1
            ans.append(cur[idx:])

        out = []
        for move in ans:
            out.append(str(len(move)) + " " + " ".join(map(str, move)))
        print("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
