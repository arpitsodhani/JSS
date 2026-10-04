# CLAUSE: setup_environment
import sys

def ask_from(start, step):
    values = []
    current = start
    while len(values) < 100:
        values.append(current)
        current += step
    sys.stdout.write("? {}\n".format(" ".join(map(str, values))))
    sys.stdout.flush()
    got = int(sys.stdin.readline())
    if got == -1:
        sys.exit()
    return got

# CLAUSE: solve_logic
def determine():
    a = ask_from(1, 1)
    b = ask_from(128, 128)
    low_bits = b % 128
    high_bits = a - (a % 128)
    return high_bits | low_bits

# CLAUSE: finish_program
sys.stdout.write("! {}\n".format(determine()))
sys.stdout.flush()
