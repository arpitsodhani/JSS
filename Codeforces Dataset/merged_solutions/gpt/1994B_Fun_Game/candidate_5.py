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

            tc = int(data[0])
            idx = 1
            ans = []

            for _ in range(tc):
                n = int(data[idx])
                s = data[idx + 1]
                t = data[idx + 2]
                idx += 3

                p = s.find('1')
                if p == -1:
                    ans.append("YES" if '1' not in t else "NO")
                else:
                    ans.append("YES" if '1' not in t[:p] else "NO")

            print('\n'.join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
