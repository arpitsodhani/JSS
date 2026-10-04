# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = data[pos]
    pos += 1
    result = []
    for _ in range(tests):
        n = data[pos]
        pos += 1
        stack = []
        best = 0
        ans = []
        for _ in range(n):
            length = data[pos]
            value = data[pos + 1]
            pos += 2
            stack.append([value, length])
            while True:
                changed = False
                if len(stack) > 1 and stack[-1][0] == stack[-2][0]:
                    stack[-2][1] += stack[-1][1]
                    stack.pop()
                    changed = True
                elif len(stack) > 2 and stack[-1][0] == stack[-3][0]:
                    left_value, left_len = stack[-3]
                    middle_len = stack[-2][1]
                    right_len = stack[-1][1]
                    if middle_len < left_len and middle_len < right_len:
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append([left_value, left_len + right_len - middle_len])
                        changed = True
                if not changed:
                    break
            if stack[-1][1] > best:
                best = stack[-1][1]
            ans.append(str(best))
        result.append(" ".join(ans))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
