# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        n = int(sys.stdin.readline())

        if n == 5:
            print("01110")
            print("11011")
            print("10001")
            print("11011")
            print("01110")
        else:
            p = [
                "011100",
                "110110",
                "100010",
                "110110",
                "011100",
                "000000",
            ]
            out = []
            for i in range(n):
                row = []
                pi = i % 6
                for j in range(n):
                    row.append(p[pi][j % 6])
                out.append("".join(row))
            print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
