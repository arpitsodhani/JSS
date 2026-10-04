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
                idx += 1
                a = data[idx:idx + n]
                idx += n
                b = data[idx:idx + n]
                idx += n

                cur = a[:]
                res = 0
                ok = True

                for x in b:
                    pos = -1
                    for i, v in enumerate(cur):
                        if v <= x:
                            pos = i
                            break
                    if pos == -1:
                        ok = False
                        break
                    res += pos
                    cur.pop(pos)

                ans.append(str(res if ok else -1))

            sys.stdout.write("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
