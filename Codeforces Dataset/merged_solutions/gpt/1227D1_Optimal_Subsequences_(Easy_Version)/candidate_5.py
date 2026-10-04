# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            n = data[0]
            a = data[1:1 + n]
            m = data[1 + n]

            items = sorted([(a[i], i) for i in range(n)], key=lambda x: (-x[0], x[1]))

            ans = []
            ptr = 2 + n
            for _ in range(m):
                k = data[ptr]
                pos = data[ptr + 1]
                ptr += 2

                chosen = sorted(items[:k], key=lambda x: x[1])
                ans.append(str(chosen[pos - 1][0]))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
