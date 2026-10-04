# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    it = iter(sys.stdin.read().split())
    tests = int(next(it))
    result = []
    for _ in range(tests):
        n = int(next(it))
        s = next(it)
        left_white = 0
        prefix_white = 0
        seen_red = False
        for i in range(n):
            if s[i] == "W":
                left_white += 1
                if not seen_red:
                    prefix_white += 1
            else:
                seen_red = True
        if left_white % 2:
            result.append("NO")
            continue
        if left_white == n:
            result.append("YES")
            continue
        suffix_red = 0
        for i in range(2 * n - 1, n - 1, -1):
            if s[i] == "R":
                suffix_red += 1
            else:
                break
        half = left_white // 2
        result.append("YES" if prefix_white >= half and suffix_red >= half else "NO")
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
