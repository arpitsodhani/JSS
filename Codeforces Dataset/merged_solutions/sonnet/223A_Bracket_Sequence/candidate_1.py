# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    s = sys.stdin.read().strip()
    n = len(s)

    stack = []
    value = [0] * n
    start = [0] * n

    best_value = 0
    best_l = 0
    best_r = -1

    pairs = {')': '(', ']': '['}

    for i, ch in enumerate(s):
        if ch == '(' or ch == '[':
            stack.append(i)
        else:
            if stack and s[stack[-1]] == pairs[ch]:
                j = stack.pop()

                cur = 1 if s[j] == '[' else 0
                l = j

                if j > 0 and value[j - 1] > 0 or (j > 0 and start[j - 1] <= j - 1 and s[start[j - 1]:j]):
                    if value[j - 1] or start[j - 1] != 0 or s[j - 1] in ')]':
                        cur += value[j - 1]
                        l = start[j - 1]

                value[i] = cur
                start[i] = l

                if cur > best_value:
                    best_value = cur
                    best_l = l
                    best_r = i
            else:
                stack.clear()

    print(best_value)
    if best_r >= best_l:
        print(s[best_l:best_r + 1])
    else:
        print()

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
