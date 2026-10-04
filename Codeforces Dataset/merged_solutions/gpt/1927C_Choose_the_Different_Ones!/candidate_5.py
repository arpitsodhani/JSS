# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def solve():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            ans = []

            for _ in range(t):
                n = data[idx]
                m = data[idx + 1]
                k = data[idx + 2]
                idx += 3

                a = set()
                for x in data[idx:idx + n]:
                    if x <= k:
                        a.add(x)
                idx += n

                b = set()
                for x in data[idx:idx + m]:
                    if x <= k:
                        b.add(x)
                idx += m

                half = k // 2
                only_a = 0
                only_b = 0
                ok = True

                for x in range(1, k + 1):
                    in_a = x in a
                    in_b = x in b
                    if not in_a and not in_b:
                        ok = False
                        break
                    if in_a and not in_b:
                        only_a += 1
                    elif in_b and not in_a:
                        only_b += 1

                if ok and only_a <= half and only_b <= half:
                    ans.append("YES")
                else:
                    ans.append("NO")

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
