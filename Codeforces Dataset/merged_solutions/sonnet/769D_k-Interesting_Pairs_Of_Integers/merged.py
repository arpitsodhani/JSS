# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    k = int(tokens[1])

    bits = 14
    size = 1 << bits

    if k > bits:
        print(0)
        return

    freq = [0] * size
    present = []
    seen = [False] * size

    for token in tokens[2:2 + n]:
        x = int(token)
        freq[x] += 1
        if not seen[x]:
            seen[x] = True
            present.append(x)

    if k == 0:
        ans = 0
        for x in present:
            count = freq[x]
            ans += count * (count - 1) // 2
        print(ans)
        return

    masks = [0]
    for bit in range(bits):
        added = []
        step = 1 << bit
        for mask in masks:
            added.append(mask | step)
        masks += added
    masks = [mask for mask in masks if mask.bit_count() == k]

    ans = 0
    for x in present:
        cx = freq[x]
        for mask in masks:
            y = x ^ mask
            if x < y:
                ans += cx * freq[y]

    print(ans)


# Clause finish_program [Confidence: 0.40]
main()


