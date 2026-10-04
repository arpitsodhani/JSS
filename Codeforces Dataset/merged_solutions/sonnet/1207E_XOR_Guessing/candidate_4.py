# CLAUSE: setup_environment
import sys

def receive_after_output(prefix, values):
    line = prefix + " " + " ".join(map(str, values))
    print(line, flush=True)
    result = int(sys.stdin.readline())
    if result < 0:
        raise SystemExit
    return result

# CLAUSE: solve_logic
def solve():
    groups = (tuple(range(1, 101)), tuple(128 * k for k in range(1, 101)))
    answers = []
    for group in groups:
        answers.append(receive_after_output("?", group))
    masks = {"lo": 127, "hi": 127 << 7}
    return (answers[0] & masks["hi"]) | (answers[1] & masks["lo"])

# CLAUSE: finish_program
print("! {}".format(solve()), flush=True)
