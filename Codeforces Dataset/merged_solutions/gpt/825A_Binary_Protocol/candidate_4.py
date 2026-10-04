# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.read().split()
    if len(data) >= 2:
        s = data[1]
    else:
        s = data[0] if data else ""

    print("".join(str(len(part)) for part in s.split("0")))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
