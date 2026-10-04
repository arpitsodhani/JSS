# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            out = []

            for _ in range(t):
                n = data[idx]
                y = data[idx + 1]
                idx += 2
                a = data[idx:idx + n]
                idx += n

                m = max(a)
                freq = [0] * (m + 1)
                for v in a:
                    freq[v] += 1

                pref = [0] * (m + 1)
                for i in range(1, m + 1):
                    pref[i] = pref[i - 1] + freq[i]

                best = -10**30

                for x in range(2, m + 2):
                    total = 0
                    reusable = 0
                    q = 1
                    left = 1

                    while left <= m:
                        right = q * x
                        if right > m:
                            right = m
                        cnt = pref[right] - pref[left - 1]
                        if cnt:
                            total += q * cnt
                            if q <= m:
                                reusable += min(freq[q], cnt)
                        q += 1
                        left = right + 1

                    income = total - y * (n - reusable)
                    if income > best:
                        best = income

                out.append(str(best))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
