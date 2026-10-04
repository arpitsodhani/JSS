# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import Counter

        data = list(map(int, sys.stdin.buffer.read().split()))
        p = 0

        n = data[p]
        p += 1
        known = data[p:p + n]
        p += n

        m = data[p]
        p += 1
        audio = data[p:p + m]
        p += m
        subs = data[p:p + m]

        cnt = Counter(known)

        best_idx = 0
        best_audio = -1
        best_subs = -1

        for i in range(m):
            a = cnt[audio[i]]
            s = cnt[subs[i]]
            if a > best_audio or (a == best_audio and s > best_subs):
                best_audio = a
                best_subs = s
                best_idx = i

        print(best_idx + 1)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
