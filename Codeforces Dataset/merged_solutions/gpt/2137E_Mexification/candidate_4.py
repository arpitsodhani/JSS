# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def mex_of_counts(cnt, limit):
        for i in range(limit + 2):
            if cnt[i] == 0:
                return i
        return limit + 1

    def next_state(cnt, n):
        m = mex_of_counts(cnt, n)
        nxt = [0] * (n + 2)
        kept = 0
        for x in range(m):
            if cnt[x] == 1:
                nxt[x] = 1
                kept += 1
        if m <= n + 1:
            nxt[m] = n - kept
        return nxt

    def state_sum(cnt):
        return sum(i * c for i, c in enumerate(cnt))

    def solve_case(n, k, a):
        cnt = [0] * (n + 2)
        for x in a:
            if x <= n + 1:
                cnt[x] += 1

        seen = {}
        sums = []

        step = 0
        while step < k:
            key = tuple(cnt)
            if key in seen:
                start = seen[key]
                cycle_len = step - start
                idx = start + (k - start) % cycle_len
                return sums[idx]
            seen[key] = step
            sums.append(state_sum(cnt))
            cnt = next_state(cnt, n)
            step += 1

        return state_sum(cnt)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        t = data[0]
        idx = 1
        ans = []
        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2
            a = data[idx:idx + n]
            idx += n
            ans.append(str(solve_case(n, k, a)))
        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
