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
                c0 = int(data[idx + 1])
                c1 = int(data[idx + 2])
                h = int(data[idx + 3])
                s = data[idx + 4]
                idx += 5

                cost0 = min(c0, h + c1)
                cost1 = min(c1, h + c0)

                total = 0
                for ch in s:
                    total += cost0 if ch == '0' else cost1

                ans.append(str(total))

            print("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
