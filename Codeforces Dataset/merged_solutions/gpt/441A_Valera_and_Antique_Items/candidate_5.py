# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        if not data:
            sys.exit()

        n, v = data[0], data[1]
        pos = 2
        ans = []

        for i in range(1, n + 1):
            k = data[pos]
            pos += 1
            can = False
            for price in data[pos:pos + k]:
                if price < v:
                    can = True
            pos += k
            if can:
                ans.append(i)

        print(len(ans))
        if ans:
            print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
