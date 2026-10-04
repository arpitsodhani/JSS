# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        s = sys.stdin.readline().strip()
        mirror = {
            '0': '8',
            '3': '3',
            '4': '6',
            '5': '9',
            '6': '4',
            '7': '7',
            '8': '0',
            '9': '5',
        }

        ok = True
        for i in range(len(s)):
            if s[i] not in mirror or mirror[s[i]] != s[-1 - i]:
                ok = False
                break

        print("Yes" if ok else "No")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
