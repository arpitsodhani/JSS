# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        n, q = data[0], data[1]
        odd = 0
        even = 1
        idx = 2

        for _ in range(q):
            t = data[idx]
            idx += 1
            if t == 1:
                x = data[idx] % n
                idx += 1
                odd = (odd + x) % n
                even = (even + x) % n
                if x & 1:
                    odd, even = even, odd
            else:
                odd = (odd + 1) % n
                even = (even - 1) % n
                odd, even = even, odd

        ans = [0] * n
        cur = odd
        for boy in range(1, n + 1, 2):
            ans[cur] = boy
            cur = (cur + 2) % n

        cur = even
        for boy in range(2, n + 1, 2):
            ans[cur] = boy
            cur = (cur + 2) % n

        print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
