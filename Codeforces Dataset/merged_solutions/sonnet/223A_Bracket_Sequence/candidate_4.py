# CLAUSE: setup_environment
import sys

def main():
    s = sys.stdin.read().strip()
    pref = [0]
    for ch in s:
        pref.append(pref[-1] + (ch == "["))

# CLAUSE: solve_logic
    stack = []
    last_bad = -1
    best = 0
    ans_l = 0
    ans_r = -1

    for pos, ch in enumerate(s):
        if ch in "([":
            stack.append(pos)
        else:
            if stack and ((ch == ")" and s[stack[-1]] == "(") or (ch == "]" and s[stack[-1]] == "[")):
                stack.pop()
                left = stack[-1] + 1 if stack else last_bad + 1
                got = pref[pos + 1] - pref[left]
                if got > best:
                    best = got
                    ans_l = left
                    ans_r = pos
            else:
                stack.clear()
                last_bad = pos

# CLAUSE: finish_program
    out = [str(best), s[ans_l:ans_r + 1] if ans_r >= ans_l else ""]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
