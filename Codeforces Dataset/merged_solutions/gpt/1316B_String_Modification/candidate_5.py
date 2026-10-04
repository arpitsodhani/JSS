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
            out = []
            for _ in range(t):
                n = int(data[idx])
                s = data[idx + 1]
                idx += 2

                best = None
                best_k = 1

                for k in range(1, n + 1):
                    prefix = s[:k - 1]
                    suffix = s[k - 1:]
                    if (n - k) % 2 == 0:
                        candidate = suffix + prefix[::-1]
                    else:
                        candidate = suffix + prefix

                    if best is None or candidate < best:
                        best = candidate
                        best_k = k

                out.append(best)
                out.append(str(best_k))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
