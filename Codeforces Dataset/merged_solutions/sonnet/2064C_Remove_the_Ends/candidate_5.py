# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    raw = sys.stdin.buffer.read().split()
    k = 0
    t = int(raw[k])
    k += 1
    answers = []

    for _ in range(t):
        n = int(raw[k])
        k += 1
        a = [int(x) for x in raw[k:k + n]]
        k += n

        neg_after = [0]
        total = 0
        for x in reversed(a):
            if x < 0:
                total += -x
            neg_after.append(total)
        neg_after.reverse()

        positives = 0
        best = neg_after[0]
        for i, x in enumerate(a, 1):
            if x > 0:
                positives += x
            score = positives + neg_after[i]
            if score > best:
                best = score

        answers.append(str(best))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
