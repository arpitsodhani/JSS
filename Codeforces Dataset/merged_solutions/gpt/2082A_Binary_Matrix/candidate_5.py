# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = sys.stdin.read().strip().split()
            t = int(data[0])
            idx = 1
            ans = []
            for _ in range(t):
                n = int(data[idx])
                m = int(data[idx + 1])
                idx += 2

                bad_rows = 0
                col = [0] * m

                for _ in range(n):
                    s = data[idx]
                    idx += 1
                    r = 0
                    for j, ch in enumerate(s):
                        v = ord(ch) - 48
                        r ^= v
                        col[j] ^= v
                    bad_rows += r

                bad_cols = sum(col)
                ans.append(str(max(bad_rows, bad_cols)))

            print("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
