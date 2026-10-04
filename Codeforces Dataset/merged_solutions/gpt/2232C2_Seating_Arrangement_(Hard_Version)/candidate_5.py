# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            data = sys.stdin.buffer.read().split()
            t = int(data[0])
            idx = 1
            out = []

            for _ in range(t):
                n = int(data[idx])
                x = int(data[idx + 1])
                s = int(data[idx + 2])
                u = data[idx + 3].decode()
                idx += 4

                low = 0
                high = 0
                ans = 0
                total = x * s

                for c in u:
                    if c == 'A':
                        if ans == total:
                            continue
                        ans += 1
                        if ans > low * s:
                            low += 1
                        if high < x:
                            high += 1
                    elif c == 'I':
                        if low == x:
                            continue
                        ans += 1
                        low += 1
                        if high < x:
                            high += 1
                    else:
                        if ans == high * s:
                            continue
                        ans += 1
                        if ans > low * s:
                            low += 1

                out.append(str(ans))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
