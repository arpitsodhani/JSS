# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return

        n = int(data[0])
        m = int(data[1])
        strings = data[2:2 + n]

        def key(item):
            s, idx = item
            return tuple(ord(c) if i % 2 == 0 else -ord(c) for i, c in enumerate(s))

        order = sorted(((strings[i], i + 1) for i in range(n)), key=key)
        print(*[idx for _, idx in order])

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
