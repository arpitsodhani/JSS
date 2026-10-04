# Clause setup_environment [Confidence: 0.40]
import sys

def receive():
    return int(sys.stdin.readline())

def send(text):
    print(text, flush=True)


# Clause solve_logic [Confidence: 0.80]
def solve():
    start = int(sys.stdin.readline())
    small_steps = 10
    big_step = 1010
    seen = {start: 0}
    current = start

    for step in range(1, small_steps + 1):
        current = ask("+ 1")
        if current == start:
            print("! " + str(step), flush=True)
            return
        if current not in seen:
            seen[current] = step

    for jump in range(1, 991):
        current = ask("- " + str(big_step))
        if current in seen:
            answer = seen[current] + jump * big_step - small_steps
            if answer > 0:
                print("! " + str(answer), flush=True)
                return


# Clause finish_program [Confidence: 0.80]
solve()


