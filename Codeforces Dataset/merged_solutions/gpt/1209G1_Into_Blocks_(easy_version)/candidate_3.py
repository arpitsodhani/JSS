# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n = data[0]
        a = data[2:2 + n]

        first = {}
        last = {}
        cnt = {}

        for i, x in enumerate(a):
            if x not in first:
                first[x] = i
            last[x] = i
            cnt[x] = cnt.get(x, 0) + 1

        intervals = sorted((first[x], last[x], cnt[x]) for x in first)

        ans = 0
        cur_end = -1
        total = 0
        best = 0

        for l, r, c in intervals:
            if l > cur_end:
                if total:
                    ans += total - best
                cur_end = r
                total = c
                best = c
            else:
                if r > cur_end:
                    cur_end = r
                total += c
                if c > best:
                    best = c

        if total:
            ans += total - best

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
