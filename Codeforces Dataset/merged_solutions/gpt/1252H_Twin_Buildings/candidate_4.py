# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = sys.stdin.buffer.read().split()
    if not data:
        exit()

    n = int(data[0])
    rects = []
    ans2 = 0
    p = 1

    for _ in range(n):
        l = int(data[p])
        w = int(data[p + 1])
        p += 2
        a, b = sorted((l, w))
        rects.append((a, b))
        ans2 = max(ans2, l * w)

    rects.sort(reverse=True)

    best_b = 0
    for a, b in rects:
        if best_b:
            ans2 = max(ans2, 2 * a * min(b, best_b))
        if b > best_b:
            best_b = b

    print(f"{ans2 // 2}.{5 if ans2 % 2 else 0}")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
