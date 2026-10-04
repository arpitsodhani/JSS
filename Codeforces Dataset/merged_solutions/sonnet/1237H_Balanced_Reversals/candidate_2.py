# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def kind(p):
    if p[0] == p[1]:
        return p
    return "M"

def swapped(p):
    return p[1] + p[0]

def turn_prefix(v, length):
    part = v[:length]
    part.reverse()
    for i, item in enumerate(part):
        v[i] = swapped(item)

def build_ops(a, b):
    m = len(a) // 2
    cur = [a[i:i + 2] for i in range(0, len(a), 2)]
    want = [b[i:i + 2] for i in range(0, len(b), 2)]

    ca = {"00": 0, "11": 0, "M": 0}
    cb = {"00": 0, "11": 0, "M": 0}

    for p in cur:
        ca[kind(p)] += 1
    for p in want:
        cb[kind(p)] += 1

    if ca != cb:
        return None

    ans = []
    for pos in range(m - 1, -1, -1):
        if cur[pos] == want[pos]:
            continue

        need = kind(want[pos])
        pick = -1

        for i in range(pos + 1):
            if kind(cur[i]) != need:
                continue
            if need != "M":
                pick = i
                break
            if i == 0:
                if swapped(cur[i]) == want[pos]:
                    pick = i
                    break
            elif cur[i] == want[pos]:
                pick = i
                break

        if pick == -1:
            for i in range(pos + 1):
                if kind(cur[i]) == need:
                    pick = i
                    break
            ans.append(2)
            turn_prefix(cur, 1)

        if pick != 0:
            ans.append(2 * (pick + 1))
            turn_prefix(cur, pick + 1)

        ans.append(2 * (pos + 1))
        turn_prefix(cur, pos + 1)

    return ans

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    ptr = 1
    out = []
    for _ in range(t):
        a = data[ptr]
        b = data[ptr + 1]
        ptr += 2
        res = build_ops(a, b)
        if res is None:
            out.append("-1")
        else:
            out.append(str(len(res)))
            out.append(" ".join(map(str, res)) if res else "")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
