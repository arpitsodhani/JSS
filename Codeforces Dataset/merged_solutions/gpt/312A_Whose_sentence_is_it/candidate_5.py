# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = sys.stdin.read().splitlines()
        if not data:
            sys.exit()

        n = int(data[0])
        out = []

        for i in range(1, n + 1):
            s = data[i]
            rainbow = s.startswith("miao.")
            freda = s.endswith("lala.")

            if freda and not rainbow:
                out.append("Freda's")
            elif rainbow and not freda:
                out.append("Rainbow's")
            else:
                out.append("OMG>.< I don't know!")

        print("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
