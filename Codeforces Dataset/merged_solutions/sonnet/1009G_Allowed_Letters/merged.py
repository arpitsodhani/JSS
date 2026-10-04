# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    s = tokens[0].decode()
    n = len(s)
    m = int(tokens[1]) if len(tokens) > 1 else 0

    full = 63
    allowed = [full] * n
    p = 2
    for _ in range(m):
        pos = int(tokens[p]) - 1
        letters = tokens[p + 1]
        p += 2
        mask = 0
        for b in letters:
            mask |= 1 << (b - 97)
        allowed[pos] = mask

    counts = [0] * 6
    for ch in s:
        counts[ord(ch) - 97] += 1

    need = [0] * 64
    for mask in allowed:
        need[mask] += 1

    demand = need[:]
    for bit in range(6):
        step = 1 << bit
        for mask in range(64):
            if mask & step:
                demand[mask] += demand[mask ^ step]

    cap = [0] * 64
    for mask in range(64):
        total = 0
        for c in range(6):
            if mask & (1 << c):
                total += counts[c]
        cap[mask] = total

    supers = [[] for _ in range(64)]
    for sub in range(64):
        missing = full ^ sub
        x = missing
        while True:
            supers[sub].append(sub | x)
            if x == 0:
                break
            x = (x - 1) & missing

    by_letter = [[mask for mask in range(1, 64) if mask & (1 << c)] for c in range(6)]

    def feasible():
        for mask in range(1, 64):
            if demand[mask] > cap[mask]:
                return False
        return True

    if not feasible():
        print("Impossible")
        return

    ans = []
    for mask in allowed:
        for sup in supers[mask]:
            demand[sup] -= 1

        ok = False
        for c in range(6):
            if counts[c] and (mask & (1 << c)):
                counts[c] -= 1
                for sup in by_letter[c]:
                    cap[sup] -= 1
                if feasible():
                    ans.append(chr(97 + c))
                    ok = True
                    break
                for sup in by_letter[c]:
                    cap[sup] += 1
                counts[c] += 1

        if not ok:
            print("Impossible")
            return

    print("".join(ans))


# Clause finish_program [Confidence: 0.40]
if __name__ == "__main__":
    main()


