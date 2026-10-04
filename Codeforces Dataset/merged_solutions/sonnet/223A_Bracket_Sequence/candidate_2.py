# CLAUSE: setup_environment
import sys

def main():
    s = sys.stdin.read().strip()
    n = len(s)
    pref = [0] * (n + 1)
    for i, ch in enumerate(s):
        pref[i + 1] = pref[i] + (1 if ch == "[" else 0)

# CLAUSE: solve_logic
    stack = [-1]
    best = 0
    best_l = 0
    best_r = -1
    pairs = {")": "(", "]": "["}

    for i, ch in enumerate(s):
        if ch == "(" or ch == "[":
            stack.append(i)
        elif len(stack) > 1 and s[stack[-1]] == pairs[ch]:
            stack.pop()
            left = stack[-1] + 1
            score = pref[i + 1] - pref[left]
            if score > best:
                best = score
                best_l = left
                best_r = i
        else:
            stack = [i]

# CLAUSE: finish_program
    sys.stdout.write(str(best) + "\n")
    if best_r >= best_l:
        sys.stdout.write(s[best_l:best_r + 1] + "\n")
    else:
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
