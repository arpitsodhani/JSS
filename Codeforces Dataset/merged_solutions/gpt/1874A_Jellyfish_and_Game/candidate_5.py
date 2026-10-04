# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            out = []

            for _ in range(t):
                n, m, k = data[idx], data[idx + 1], data[idx + 2]
                idx += 3
                a = data[idx:idx + n]
                idx += n
                b = data[idx:idx + m]
                idx += m

                sa = sum(a)

                amin = min(a)
                amax = max(a)
                bmin = min(b)
                bmax = max(b)

                if bmax > amin:
                    sa += bmax - amin
                    amax = max(amax, bmax)
                    bmin = min(bmin, amin)

                if k % 2 == 0:
                    if amax > bmin:
                        sa -= amax - bmin

                out.append(str(sa))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
