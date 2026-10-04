# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        n, k, d = map(int, input().split())

        cnt = 1
        for _ in range(d):
            cnt *= k
            if cnt >= n:
                break

        if cnt < n:
            print(-1)
        else:
            ans = []
            for day in range(d):
                div = k ** (d - day - 1)
                row = []
                for i in range(n):
                    row.append(str((i // div) % k + 1))
                ans.append(" ".join(row))
            print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
