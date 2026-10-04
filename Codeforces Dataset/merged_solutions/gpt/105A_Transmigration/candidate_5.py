# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().split()
        if not data:
            sys.exit()

        it = iter(data)
        n = int(next(it))
        m = int(next(it))
        kstr = next(it)

        if '.' in kstr:
            a, b = kstr.split('.', 1)
            num = int(a + b)
            den = 10 ** len(b)
        else:
            num = int(kstr)
            den = 1

        skills = {}

        for _ in range(n):
            name = next(it)
            level = int(next(it))
            new_level = level * num // den
            if new_level >= 100:
                skills[name] = new_level

        for _ in range(m):
            name = next(it)
            if name not in skills:
                skills[name] = 0

        out = [str(len(skills))]
        for name in sorted(skills):
            out.append(f"{name} {skills[name]}")

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
