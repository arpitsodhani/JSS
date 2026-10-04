# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import Counter

        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        a = data[1:]

        cnt = Counter(a)
        ans = 0
        carry = 0
        prev = None

        for e in sorted(cnt):
            if prev is not None:
                gap = e - prev
                while carry and gap:
                    ans += carry & 1
                    carry >>= 1
                    gap -= 1
            carry += cnt[e]
            ans += carry & 1
            carry >>= 1
            prev = e

        while carry:
            ans += carry & 1
            carry >>= 1

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
