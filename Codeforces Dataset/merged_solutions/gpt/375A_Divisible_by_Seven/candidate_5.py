# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from itertools import permutations

        s = sys.stdin.readline().strip()

        need = {'1': 1, '6': 1, '8': 1, '9': 1}
        rest = []
        zeros = 0

        for c in s:
            if c in need and need[c] > 0:
                need[c] -= 1
            elif c == '0':
                zeros += 1
            else:
                rest.append(c)

        rem = 0
        for c in rest:
            rem = (rem * 10 + int(c)) % 7

        chosen = None
        for p in permutations("1689"):
            t = ''.join(p)
            if (rem * 10000 + int(t)) % 7 == 0:
                chosen = t
                break

        print(''.join(rest) + chosen + '0' * zeros)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
