# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        n = data[0]
        p = data[1:]

        visited = [False] * n
        lengths = []

        for i in range(n):
            if not visited[i]:
                cur = i
                cnt = 0
                while not visited[cur]:
                    visited[cur] = True
                    cnt += 1
                    cur = p[cur] - 1
                lengths.append(cnt)

        lengths.sort(reverse=True)

        if len(lengths) >= 2:
            merged = lengths[0] + lengths[1]
            ans = merged * merged + sum(x * x for x in lengths[2:])
        else:
            ans = n * n

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
