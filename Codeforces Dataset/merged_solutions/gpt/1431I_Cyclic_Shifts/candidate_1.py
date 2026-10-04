# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    q = int(data[2])

    masks = [0] * (m * 26)
    idx = 3

    bit = 1
    for _ in range(n):
        row = data[idx]
        idx += 1
        base = 0
        for ch in row:
            masks[base + ch - 97] |= bit
            base += 26
        bit <<= 1

    ans = []
    for _ in range(q):
        s = data[idx]
        idx += 1

        first = masks[s[0] - 97]
        if first == 0:
            ans.append("-1")
            continue

        best = first
        cost = 0
        ok = True
        base = 26

        for ch in s[1:]:
            cur = masks[base + ch - 97]
            if cur == 0:
                ok = False
                break

            inter = best & cur
            if inter:
                best = inter
            else:
                cost += 1
                best = cur

            base += 26

        ans.append(str(cost) if ok else "-1")

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
