# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    sys.setrecursionlimit(1000000)

    def zero_rectangles(grid, n, m):
        h = [0] * m
        ans = 0
        for row in grid:
            for j, c in enumerate(row):
                if c == 48:
                    h[j] += 1
                else:
                    h[j] = 0
            st = []
            cur = 0
            for v in h:
                cnt = 1
                while st and st[-1][0] >= v:
                    ph, pc = st.pop()
                    cur -= ph * pc
                    cnt += pc
                st.append((v, cnt))
                cur += v * cnt
                ans += cur
        return ans

    def main():
        data = sys.stdin.buffer.read().split()
        if not data:
            return

        n = int(data[0])
        m = int(data[1])
        k = int(data[2])
        grid = data[3:3 + n]

        if k == 0:
            print(zero_rectangles(grid, n, m))
            return

        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            prev = pref[i - 1]
            cur = pref[i]
            run = 0
            row = grid[i - 1]
            for j, c in enumerate(row, 1):
                run += c & 1
                cur[j] = prev[j] + run

        if pref[n][m] < k:
            print(0)
            return

        ans = 0
        kk = k
        kr = range(kk + 1)

        def solve(r1, r2, c1, c2):
            nonlocal ans

            if r1 == r2 and c1 == c2:
                if pref[r2][c2] - pref[r2][c2 - 1] - pref[r2 - 1][c2] + pref[r2 - 1][c2 - 1] == kk:
                    ans += 1
                return

            if r2 - r1 > c2 - c1:
                mid = (r1 + r2) >> 1
                smid = pref[mid]

                for x in range(c1, c2 + 1):
                    xm = x - 1
                    up = [r1] * (kk + 1)
                    down = [r2] * (kk + 1)
                    a = [0] * (kk + 1)
                    b = [0] * (kk + 1)

                    for y in range(x, c2 + 1):
                        base = smid[y] - smid[xm]

                        for lim in kr:
                            u = up[lim]
                            while u <= mid:
                                row = pref[u - 1]
                                if base - row[y] + row[xm] <= lim:
                                    break
                                u += 1
                            up[lim] = u
                            a[lim] = mid - u + 1

                            d = down[lim]
                            while d > mid:
                                row = pref[d]
                                if row[y] - row[xm] - base <= lim:
                                    break
                                d -= 1
                            down[lim] = d
                            b[lim] = d - mid

                        prev_a = 0
                        add = 0
                        for t in kr:
                            exact_a = a[t] - prev_a
                            prev_a = a[t]
                            need = kk - t
                            exact_b = b[need]
                            if need:
                                exact_b -= b[need - 1]
                            add += exact_a * exact_b
                        ans += add

                solve(r1, mid, c1, c2)
                solve(mid + 1, r2, c1, c2)

            else:
                mid = (c1 + c2) >> 1

                for x in range(r1, r2 + 1):
                    row_before = pref[x - 1]
                    left = [c1] * (kk + 1)
                    right = [c2] * (kk + 1)
                    a = [0] * (kk + 1)
                    b = [0] * (kk + 1)

                    for y in range(x, r2 + 1):
                        row_after = pref[y]
                        base = row_after[mid] - row_before[mid]

                        for lim in kr:
                            l = left[lim]
                            while l <= mid:
                                if base - row_after[l - 1] + row_before[l - 1] <= lim:
                                    break
                                l += 1
                            left[lim] = l
                            a[lim] = mid - l + 1

                            r = right[lim]
                            while r > mid:
                                if row_after[r] - row_before[r] - base <= lim:
                                    break
                                r -= 1
                            right[lim] = r
                            b[lim] = r - mid

                        prev_a = 0
                        add = 0
                        for t in kr:
                            exact_a = a[t] - prev_a
                            prev_a = a[t]
                            need = kk - t
                            exact_b = b[need]
                            if need:
                                exact_b -= b[need - 1]
                            add += exact_a * exact_b
                        ans += add

                solve(r1, r2, c1, mid)
                solve(r1, r2, mid + 1, c2)

        solve(1, n, 1, m)
        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
