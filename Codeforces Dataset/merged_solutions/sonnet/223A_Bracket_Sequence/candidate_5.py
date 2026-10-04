# CLAUSE: setup_environment
import sys

def count_squares(prefix, left, right):
    return prefix[right + 1] - prefix[left]

def main():
    s = sys.stdin.read().strip()
    n = len(s)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if s[i] == "[" else 0)

# CLAUSE: solve_logic
    opens = []
    barriers = [-1]
    best_count = 0
    best_range = (0, -1)

    for i in range(n):
        ch = s[i]
        if ch == "(" or ch == "[":
            opens.append(i)
        else:
            ok = bool(opens) and ((ch == ")" and s[opens[-1]] == "(") or (ch == "]" and s[opens[-1]] == "["))
            if ok:
                opens.pop()
                left_limit = opens[-1] if opens else barriers[-1]
                left = left_limit + 1
                current = count_squares(prefix, left, i)
                if current > best_count:
                    best_count = current
                    best_range = (left, i)
            else:
                opens.clear()
                barriers.append(i)

# CLAUSE: finish_program
    left, right = best_range
    sys.stdout.write(str(best_count) + "\n")
    sys.stdout.write((s[left:right + 1] if right >= left else "") + "\n")

if __name__ == "__main__":
    main()
