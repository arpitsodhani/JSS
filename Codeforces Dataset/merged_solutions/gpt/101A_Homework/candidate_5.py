# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import Counter

        data = sys.stdin.read().split()

        if len(data) >= 2:
            s = data[0]
            k = int(data[1])
        else:
            token = data[0]
            i = len(token) - 1
            while i >= 0 and token[i].isdigit():
                i -= 1
            s = token[:i + 1]
            k = int(token[i + 1:])

        cnt = Counter(s)
        removed = set()

        for ch, c in sorted(cnt.items(), key=lambda x: x[1]):
            if c <= k:
                k -= c
                removed.add(ch)

        ans = ''.join(ch for ch in s if ch not in removed)
        print(len(set(ans)))
        if ans:
            print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
