# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_left

        def find_subsequence(a, need, decreasing=False):
            n = len(a)
            tails = []
            tails_idx = []
            parent = [-1] * n

            for i, x in enumerate(a):
                v = -x if decreasing else x
                pos = bisect_left(tails, v)

                if pos:
                    parent[i] = tails_idx[pos - 1]

                if pos == len(tails):
                    tails.append(v)
                    tails_idx.append(i)
                else:
                    tails[pos] = v
                    tails_idx[pos] = i

            if len(tails) < need:
                return None

            cur = tails_idx[need - 1]
            res = []
            while cur != -1:
                res.append(cur + 1)
                cur = parent[cur]
            res.reverse()
            return res[:need]

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            t = data[0]
            ptr = 1
            out = []

            for _ in range(t):
                n = data[ptr]
                ptr += 1
                m = n * n + 1
                p = data[ptr:ptr + m]
                ptr += m

                ans = find_subsequence(p, n + 1, False)
                if ans is None:
                    ans = find_subsequence(p, n + 1, True)

                out.append(" ".join(map(str, ans)))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
