# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import defaultdict

        data = sys.stdin.buffer.read().split()
        n = int(data[0])
        full = (1 << 26) - 1

        cnt = [defaultdict(int) for _ in range(26)]
        ans = 0

        for s in data[1:]:
            parity = 0
            used = 0
            for ch in s:
                b = 1 << (ch - 97)
                parity ^= b
                used |= b

            missing = full ^ used
            m = missing
            while m:
                bit = m & -m
                c = bit.bit_length() - 1
                target = parity ^ (full ^ bit)
                ans += cnt[c][target]
                m -= bit

            m = missing
            while m:
                bit = m & -m
                c = bit.bit_length() - 1
                cnt[c][parity] += 1
                m -= bit

        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
