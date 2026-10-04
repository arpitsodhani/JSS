# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, m, k = data[0], data[1], data[2]
        N = n - k + 1
        items = []
        p = 3

        for _ in range(m):
            l, r = data[p], data[p + 1]
            p += 2
            pieces = []
            P = max(1, l - k + 1)
            Q = min(N, r)
            if P <= Q:
                t = r - k + 1

                L = P
                R = min(Q, t, l)
                if L <= R:
                    pieces.append((L, R, 1, k - l))

                L = max(P, l + 1)
                R = min(Q, t)
                if L <= R:
                    pieces.append((L, R, 0, k))

                L = max(P, t + 1)
                R = min(Q, l)
                if L <= R:
                    pieces.append((L, R, 0, r - l + 1))

                L = max(P, t, l) + 1
                R = Q
                if L <= R:
                    pieces.append((L, R, -1, r + 1))

            items.append((l, r, pieces))

        ans = 0

        for x in range(1, N + 1):
            da = [0] * (N + 2)
            dc = [0] * (N + 2)
            base = 0
            xe = x + k - 1

            for l, r, pieces in items:
                a = l if l > x else x
                bnd = r if r < xe else xe
                b = bnd - a + 1 if a <= bnd else 0
                base += b

                for L, R, s, c0 in pieces:
                    c = c0 - b
                    if s == 0:
                        if c > 0:
                            dc[L] += c
                            dc[R + 1] -= c
                    elif s == 1:
                        t = -c + 1
                        if L < t:
                            L = t
                        if L <= R:
                            da[L] += 1
                            da[R + 1] -= 1
                            dc[L] += c
                            dc[R + 1] -= c
                    else:
                        t = c - 1
                        if R > t:
                            R = t
                        if L <= R:
                            da[L] -= 1
                            da[R + 1] += 1
                            dc[L] += c
                            dc[R + 1] -= c

            dc[1] += base
            dc[N + 1] -= base

            ca = 0
            cc = 0
            for y in range(1, N + 1):
                ca += da[y]
                cc += dc[y]
                val = ca * y + cc
                if val > ans:
                    ans = val

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
