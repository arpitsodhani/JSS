# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 10**9 + 7

        data = sys.stdin.read().split()
        n = int(data[0])
        s = data[1]
        a = list(map(int, data[2:28]))

        ways = [0] * (n + 1)
        min_parts = [10**9] * (n + 1)
        ways[0] = 1
        min_parts[0] = 0
        max_len = 0

        for i in range(1, n + 1):
            limit = n
            for j in range(i, 0, -1):
                c = ord(s[j - 1]) - 97
                limit = min(limit, a[c])
                length = i - j + 1
                if length > limit:
                    break
                ways[i] = (ways[i] + ways[j - 1]) % MOD
                min_parts[i] = min(min_parts[i], min_parts[j - 1] + 1)
                if length > max_len:
                    max_len = length

        print(ways[n])
        print(max_len)
        print(min_parts[n])

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
