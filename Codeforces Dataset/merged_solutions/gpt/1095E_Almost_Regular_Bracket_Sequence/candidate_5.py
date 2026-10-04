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
            n = int(data[0])
            s = data[1]

            pref = [0] * (n + 1)
            for i, ch in enumerate(s, 1):
                pref[i] = pref[i - 1] + (1 if ch == '(' else -1)

            total = pref[n]
            if total not in (2, -2):
                print(0)
                return

            suffix_min = [0] * (n + 2)
            suffix_min[n] = pref[n]
            for i in range(n - 1, 0, -1):
                suffix_min[i] = min(pref[i], suffix_min[i + 1])

            ans = 0
            prefix_ok = True

            if total == 2:
                for i, ch in enumerate(s, 1):
                    if prefix_ok and ch == '(' and suffix_min[i] >= 2:
                        ans += 1
                    if pref[i] < 0:
                        prefix_ok = False
            else:
                for i, ch in enumerate(s, 1):
                    if prefix_ok and ch == ')' and suffix_min[i] >= -2:
                        ans += 1
                    if pref[i] < 0:
                        prefix_ok = False

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
