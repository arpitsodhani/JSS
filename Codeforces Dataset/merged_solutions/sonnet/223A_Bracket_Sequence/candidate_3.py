# CLAUSE: setup_environment
import sys

def main():
    s = sys.stdin.read().strip()
    n = len(s)
    length = [0] * n
    score = [0] * n
    start = [0] * n

# CLAUSE: solve_logic
    best = 0
    best_l = 0
    best_r = -1

    for i in range(n):
        ch = s[i]
        j = -1
        if ch == ")" or ch == "]":
            need = "(" if ch == ")" else "["
            if i > 0 and s[i - 1] == need:
                j = i - 1
            elif i > 0 and length[i - 1] > 0:
                k = i - length[i - 1] - 1
                if k >= 0 and s[k] == need:
                    j = k

        if j != -1:
            base_len = i - j + 1
            base_score = 1 if s[j] == "[" else 0
            if j > 0 and length[j - 1] > 0:
                length[i] = base_len + length[j - 1]
                score[i] = base_score + score[i - 1] + score[j - 1] - (score[i - 1] if j == i - 1 else score[i - 1])
            else:
                length[i] = base_len
                score[i] = base_score + (score[i - 1] if j != i - 1 else 0)

            if j != i - 1:
                score[i] = base_score + score[i - 1]
                if j > 0 and length[j - 1] > 0:
                    score[i] += score[j - 1]

            start[i] = i - length[i] + 1
            if score[i] > best:
                best = score[i]
                best_l = start[i]
                best_r = i

# CLAUSE: finish_program
    sys.stdout.write(str(best) + "\n")
    sys.stdout.write((s[best_l:best_r + 1] if best_r >= best_l else "") + "\n")

if __name__ == "__main__":
    main()
