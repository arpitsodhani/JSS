# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def label(x):
    return x if x[0] == x[1] else "M"

def revpair(x):
    return (x[1], x[0])

def reverse_even_prefix(pairs, upto):
    left = 0
    right = upto - 1
    while left < right:
        pairs[left], pairs[right] = revpair(pairs[right]), revpair(pairs[left])
        left += 1
        right -= 1
    if left == right:
        pairs[left] = revpair(pairs[left])

def as_text(p):
    return p[0] + p[1]

def plan(a, b):
    cur = [(a[i], a[i + 1]) for i in range(0, len(a), 2)]
    dst = [(b[i], b[i + 1]) for i in range(0, len(b), 2)]

    if Counter(label(p) for p in cur) != Counter(label(p) for p in dst):
        return None

    ops = []
    last = len(cur) - 1

    while last >= 0:
        if cur[last] == dst[last]:
            last -= 1
            continue

        need = label(dst[last])
        chosen = -1

        for i, p in enumerate(cur[:last + 1]):
            if label(p) != need:
                continue
            if need != "M":
                chosen = i
                break
            if i == 0 and revpair(p) == dst[last]:
                chosen = i
                break
            if i > 0 and p == dst[last]:
                chosen = i
                break

        if chosen < 0:
            for i, p in enumerate(cur[:last + 1]):
                if label(p) == need:
                    chosen = i
                    break
            ops.append(2)
            reverse_even_prefix(cur, 1)

        if chosen:
            ops.append((chosen + 1) * 2)
            reverse_even_prefix(cur, chosen + 1)

        ops.append((last + 1) * 2)
        reverse_even_prefix(cur, last + 1)
        last -= 1

    return ops

# CLAUSE: finish_program
def main():
    items = sys.stdin.read().split()
    if not items:
        return
    total = int(items[0])
    pos = 1
    lines = []
    for _ in range(total):
        answer = plan(items[pos], items[pos + 1])
        pos += 2
        if answer is None:
            lines.append("-1")
        else:
            lines.append(str(len(answer)))
            lines.append(" ".join(str(x) for x in answer))
    print("\n".join(lines))

if __name__ == "__main__":
    main()
