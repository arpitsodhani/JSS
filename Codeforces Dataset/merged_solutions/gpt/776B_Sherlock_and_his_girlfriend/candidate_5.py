# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        n = int(sys.stdin.readline())
        m = n + 1

        is_prime = [True] * (m + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= m:
            if is_prime[p]:
                for x in range(p * p, m + 1, p):
                    is_prime[x] = False
            p += 1

        if n <= 2:
            print(1)
            print(" ".join(["1"] * n))
        else:
            print(2)
            print(" ".join("1" if is_prime[i] else "2" for i in range(2, m + 1)))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
