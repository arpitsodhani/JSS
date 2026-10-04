# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = sys.stdin.read().strip().split()
            if not data:
                return

            t = int(data[0])
            idx = 1
            ans = []

            for _ in range(t):
                n = int(data[idx])
                x = int(data[idx + 1])
                s = data[idx + 2]
                idx += 3

                l = 0
                for i in range(x - 2, -1, -1):
                    if s[i] == '#':
                        l = i + 1
                        break

                r = n + 1
                for i in range(x, n):
                    if s[i] == '#':
                        r = i + 1
                        break

                ans.append(str(max(min(x, n - r + 2), min(l + 1, n - x + 1))))

            print("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
