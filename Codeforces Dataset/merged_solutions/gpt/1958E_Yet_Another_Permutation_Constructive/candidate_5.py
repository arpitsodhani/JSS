# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def build(n, k):
            if k == 1:
                return list(range(1, n + 1))

            m = (1 << (k - 2)) + 1
            q = build(m, k - 1)

            low_count = n - m
            survivors = [low_count + x for x in q]

            res = []
            filler = 1

            for i in range(m - 1):
                res.append(survivors[i])
                res.append(filler)
                filler += 1

            res.append(survivors[-1])

            for x in range(low_count, filler - 1, -1):
                res.append(x)

            return res

        def possible(n, k):
            if k == 0:
                return n == 1
            if n <= 1:
                return False
            return k <= ((n - 1).bit_length() - 1) + 1

        def main():
            data = list(map(int, sys.stdin.read().split()))
            if not data:
                return

            if len(data) >= 3 and len(data) == 1 + 2 * data[0]:
                pairs = [(data[i], data[i + 1]) for i in range(1, len(data), 2)]
            else:
                pairs = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]

            out = []
            for n, k in pairs:
                if not possible(n, k):
                    out.append("-1")
                elif k == 0:
                    out.append("1")
                else:
                    out.append(" ".join(map(str, build(n, k))))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
