# Clause setup_environment [Confidence: 0.40]
import sys

def main():
    s = sys.stdin.read().strip()
    n = len(s)
    pref = [0] * (n + 1)
    for i, ch in enumerate(s):
        pref[i + 1] = pref[i] + (1 if ch == "[" else 0)


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.60]
    sys.stdout.write(str(best) + "\n")
    sys.stdout.write((s[best_l:best_r + 1] if best_r >= best_l else "") + "\n")

if __name__ == "__main__":
    main()


