# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    blocks = []
    for x in a:
        blocks.append([x, 1])
        while len(blocks) >= 2:
            s1, c1 = blocks[-2]
            s2, c2 = blocks[-1]
            if s1 * c2 <= s2 * c1:
                break
            blocks[-2] = [s1 + s2, c1 + c2]
            blocks.pop()
    out = []
    for s, c in blocks:
        val = s / c
        out.extend((f'{val:.9f}' for _ in range(c)))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
