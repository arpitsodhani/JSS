# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from bisect import bisect_left, bisect_right

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, k = data[0], data[1]
        ls = []
        rs = []
        min_len = 10**30
        max_r = 0

        p = 2
        for _ in range(n):
            l = data[p]
            r = data[p + 1]
            p += 2
            ls.append(l)
            rs.append(r)
            length = r - l
            if length < min_len:
                min_len = length
            if r > max_r:
                max_r = r

        limit = max_r + k
        lucky = []

        stack = [4, 7]
        while stack:
            x = stack.pop()
            if x > limit:
                continue
            lucky.append(x)
            stack.append(x * 10 + 4)
            stack.append(x * 10 + 7)

        lucky.sort()

        if not lucky:
            print(0)
            return

        ls.sort()
        rs.sort()

        pref_l = [0]
        for x in ls:
            pref_l.append(pref_l[-1] + x)

        pref_r = [0]
        for x in rs:
            pref_r.append(pref_r[-1] + x)

        total_l = pref_l[-1]

        def cost(a, b):
            cr = bisect_left(rs, b)
            res = b * cr - pref_r[cr]

            pos = bisect_right(ls, a)
            cl = n - pos
            res += total_l - pref_l[pos] - a * cl

            return res

        ans = 0
        left = 0

        for right, b in enumerate(lucky):
            while left <= right and (b - lucky[left] > min_len or cost(lucky[left], b) > k):
                left += 1
            if left <= right:
                cur = right - left + 1
                if cur > ans:
                    ans = cur

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
