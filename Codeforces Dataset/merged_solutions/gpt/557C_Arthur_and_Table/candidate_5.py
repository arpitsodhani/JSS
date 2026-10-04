# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        l = data[1:1 + n]
        d = data[1 + n:1 + 2 * n]

        costs_sorted = sorted(set(d))
        idx = {v: i + 1 for i, v in enumerate(costs_sorted)}
        m = len(costs_sorted)

        bit_cnt = [0] * (m + 1)
        bit_sum = [0] * (m + 1)

        def add(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def pref(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def sum_smallest(k):
            if k <= 0:
                return 0
            pos = 0
            step = 1 << (m.bit_length() - 1)
            rem = k
            while step:
                nxt = pos + step
                if nxt <= m and bit_cnt[nxt] < rem:
                    rem -= bit_cnt[nxt]
                    pos = nxt
                step >>= 1
            return pref(bit_sum, pos) + rem * costs_sorted[pos]

        groups = {}
        for length, cost in zip(l, d):
            groups.setdefault(length, []).append(cost)

        total_sum = sum(d)
        prefix_count = 0
        prefix_sum = 0
        ans = total_sum

        for length in sorted(groups):
            g = groups[length]
            cnt = len(g)
            cur_sum = sum(g)
            higher_sum = total_sum - prefix_sum - cur_sum
            need = prefix_count - cnt + 1
            ans = min(ans, higher_sum + sum_smallest(need))
            for c in g:
                p = idx[c]
                add(bit_cnt, p, 1)
                add(bit_sum, p, c)
            prefix_count += cnt
            prefix_sum += cur_sum

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
