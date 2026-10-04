# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def losing(s):
            n = len(s)
            l = 0
            while l < n and s[l] == '0':
                l += 1

            r = n - 1
            while r >= l and s[r] == '1':
                r -= 1

            if (r - l + 1) % 2:
                return False

            i = l
            while i <= r:
                if s[i] != s[i + 1]:
                    return False
                i += 2

            return True

        def main():
            data = sys.stdin.read().split()
            if not data:
                return

            t = int(data[0])
            ans = []
            idx = 1

            for _ in range(t):
                n = int(data[idx])
                s = data[idx + 1]
                idx += 2
                ans.append("Bob" if losing(s) else "Alice")

            print("\n".join(ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
