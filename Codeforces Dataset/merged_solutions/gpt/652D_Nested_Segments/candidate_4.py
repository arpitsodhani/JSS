# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from bisect import bisect_left

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n = data[0]
        segments = []
        rights = []

        p = 1
        for i in range(n):
            l = data[p]
            r = data[p + 1]
            p += 2
            segments.append((l, r, i))
            rights.append(r)

        rights.sort()
        segments.sort(key=lambda x: -x[0])

        bit = [0] * (n + 2)
        ans = [0] * n

        def add(i):
            while i <= n:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for _, r, idx in segments:
            pos = bisect_left(rights, r) + 1
            ans[idx] = query(pos - 1)
            add(pos)

        sys.stdout.write("\n".join(map(str, ans)))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
