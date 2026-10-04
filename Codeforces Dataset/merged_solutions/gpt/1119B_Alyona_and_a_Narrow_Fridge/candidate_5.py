# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def can_fit(arr, h):
            b = sorted(arr, reverse=True)
            return sum(b[i] for i in range(0, len(b), 2)) <= h

        def main():
            data = list(map(int, sys.stdin.read().split()))
            n, h = data[0], data[1]
            a = data[2:]

            ans = 0
            for k in range(1, n + 1):
                if can_fit(a[:k], h):
                    ans = k
                else:
                    break

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
