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
                a = int(data[idx + 1])
                q = int(data[idx + 2])
                s = data[idx + 3]
                idx += 4

                cur = a
                reached = (a == n)

                for ch in s:
                    if ch == '+':
                        cur += 1
                    else:
                        cur -= 1
                    if cur == n:
                        reached = True

                if reached:
                    ans.append("YES")
                elif a + s.count('+') >= n:
                    ans.append("MAYBE")
                else:
                    ans.append("NO")

            print("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
