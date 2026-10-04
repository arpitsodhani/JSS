# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        n = int(data[0])
        a = list(map(int, data[1:1 + n]))
        s = data[1 + n].strip()

        total = 0
        ans = 0

        for i in range(n):
            if s[i] == '1':
                total += a[i]

        ans = total
        lower_sum = 0

        for i in range(n):
            if s[i] == '1':
                total -= a[i]
                candidate = total + lower_sum
                if candidate > ans:
                    ans = candidate
            lower_sum += a[i]

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
