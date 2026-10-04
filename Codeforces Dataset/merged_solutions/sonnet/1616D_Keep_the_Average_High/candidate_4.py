# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    tests = raw[p]
    p += 1
    answers = []

    for _ in range(tests):
        n = raw[p]
        p += 1
        arr = raw[p:p + n]
        p += n
        x = raw[p]
        p += 1

        keep = 0
        prev2_value = 0
        prev1_value = 0
        prev2_kept = False
        prev1_kept = False

        for value in arr:
            ok = True
            if prev1_kept and prev1_value + value < 2 * x:
                ok = False
            if ok and prev1_kept and prev2_kept and prev2_value + prev1_value + value < 3 * x:
                ok = False
            if ok:
                keep += 1
            prev2_value, prev1_value = prev1_value, value
            prev2_kept, prev1_kept = prev1_kept, ok

        answers.append(str(keep))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
