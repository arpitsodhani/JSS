# CLAUSE: setup_environment
import sys

read = sys.stdin.readline

def move(sign, amount):
    sys.stdout.write(sign + " " + str(amount) + "\n")
    sys.stdout.flush()
    return int(read())

# CLAUSE: solve_logic
def solve():
    origin = int(read())
    offsets = {}
    offsets[origin] = 0
    value = origin
    step = 1

    while step <= 10:
        value = move("+", 1)
        if value == origin:
            sys.stdout.write("! " + str(step) + "\n")
            sys.stdout.flush()
            return
        offsets.setdefault(value, step)
        step += 1

    jump = 1
    while jump < 991:
        value = move("-", 1010)
        stored = offsets.get(value)
        if stored is not None:
            result = stored + jump * 1010 - 10
            if result > 0:
                sys.stdout.write("! " + str(result) + "\n")
                sys.stdout.flush()
                return
        jump += 1

# CLAUSE: finish_program
solve()
