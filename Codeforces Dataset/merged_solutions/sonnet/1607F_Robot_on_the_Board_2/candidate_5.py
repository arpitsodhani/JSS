# CLAUSE: setup_environment
import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    lines = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        grid = data[idx:idx + n]
        idx += n
        total = n * m
        nxt = [-1] * total

        for r in range(n):
            base = r * m
            row = grid[r]
            for c in range(m):
                v = base + c
                b = row[c]
                if b == 76 and c:
                    nxt[v] = v - 1
                elif b == 82 and c != m - 1:
                    nxt[v] = v + 1
                elif b == 85 and r:
                    nxt[v] = v - m
                elif b == 68 and r != n - 1:
                    nxt[v] = v + m

        status = bytearray(total)
        answer = [0] * total
        stack_index = [-1] * total

        for root in range(total):
            if status[root]:
                continue
            stack = []
            cur = root
            while cur != -1 and status[cur] == 0:
                status[cur] = 1
                stack_index[cur] = len(stack)
                stack.append(cur)
                cur = nxt[cur]

            if cur != -1 and status[cur] == 1:
                first = stack_index[cur]
                cycle = len(stack) - first
                for pos in range(first, len(stack)):
                    answer[stack[pos]] = cycle
                value = cycle
                pos = first - 1
            else:
                value = answer[cur] if cur != -1 else 0
                pos = len(stack) - 1

            while pos >= 0:
                value += 1
                answer[stack[pos]] = value
                pos -= 1

            for v in stack:
                status[v] = 2
                stack_index[v] = -1

        best_pos = max(range(total), key=answer.__getitem__)
        lines.append(f"{best_pos // m + 1} {best_pos % m + 1} {answer[best_pos]}")

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
