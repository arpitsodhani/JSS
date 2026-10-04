# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            ans = []

            for _ in range(t):
                n = data[idx]
                k = data[idx + 1]
                q = data[idx + 2]
                idx += 3

                cur = 0
                total = 0

                for i in range(n):
                    if data[idx + i] <= q:
                        cur += 1
                    else:
                        if cur >= k:
                            x = cur - k + 1
                            total += x * (x + 1) // 2
                        cur = 0

                if cur >= k:
                    x = cur - k + 1
                    total += x * (x + 1) // 2

                idx += n
                ans.append(str(total))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
