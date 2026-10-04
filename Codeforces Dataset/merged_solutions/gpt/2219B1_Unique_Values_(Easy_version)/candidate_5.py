# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            t = data[0]
            pos = 1
            out = []
            for _ in range(t):
                n = data[pos]
                pos += 1
                a = data[pos:pos + 2 * n + 1]
                pos += 2 * n + 1

                positions = {}
                for i, value in enumerate(a, 1):
                    positions.setdefault(value, []).append(i)

                for inds in positions.values():
                    if len(inds) == 3:
                        out.append(f"{inds[0]} {inds[1]} {inds[2]}")
                        break

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
