# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            data = sys.stdin.read().split()
            if not data:
                return

            t = int(data[0])
            idx = 1
            out = []

            for _ in range(t):
                n = int(data[idx])
                m = int(data[idx + 1])
                k = int(data[idx + 2])
                s = data[idx + 3]
                idx += 4

                ans = 0
                zeros = 0
                i = 0

                while i < n:
                    if s[i] == '1':
                        zeros = 0
                        i += 1
                    else:
                        zeros += 1
                        if zeros == m:
                            ans += 1
                            zeros = 0
                            i += k
                        else:
                            i += 1

                out.append(str(ans))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
