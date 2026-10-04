# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        p = [0] + data[1:]

        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            pos[p[i]] = i

        left = [0] * (n + 1)
        right = [n + 1] * (n + 1)

        st = []
        for i in range(1, n + 1):
            while st and p[st[-1]] < p[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)

        st = []
        for i in range(n, 0, -1):
            while st and p[st[-1]] < p[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0

        for m in range(1, n + 1):
            mx = p[m]
            l_bound = left[m] + 1
            r_bound = right[m] - 1

            if m - l_bound <= r_bound - m:
                for i in range(l_bound, m):
                    need = mx - p[i]
                    if need > 0:
                        j = pos[need]
                        if m < j <= r_bound:
                            ans += 1
            else:
                for j in range(m + 1, r_bound + 1):
                    need = mx - p[j]
                    if need > 0:
                        i = pos[need]
                        if l_bound <= i < m:
                            ans += 1

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
