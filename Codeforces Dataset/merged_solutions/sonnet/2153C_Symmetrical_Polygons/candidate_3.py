# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(arr):
    freq = {}
    total = 0
    for v in arr:
        total += v
        freq[v] = freq.get(v, 0) + 1

    lengths = sorted(freq)
    odd = [v for v in lengths if freq[v] % 2]
    cut = 0
    start = 0
    while len(odd) - start > 2:
        cut += odd[start]
        start += 1

    active_odd = set(odd[start:])

    while cut < total:
        per = total - cut
        top = 0
        for v in reversed(lengths):
            if freq[v] - (1 if v in active_odd else 0) > 0 or v in active_odd:
                top = v
                break

        if top * 2 < per and per - cut >= 3:
            return per

        if start < len(odd):
            cut += odd[start]
            active_odd.discard(odd[start])
            start += 1
        else:
            pair = 0
            for v in lengths:
                if freq[v] >= 2:
                    pair = v
                    break
            if pair == 0:
                break
            freq[pair] -= 2
            cut += pair * 2

    return 0

# CLAUSE: finish_program
def main():
    vals = list(map(int, sys.stdin.buffer.read().split()))
    if not vals:
        return
    t = vals[0]
    i = 1
    out = []
    for _ in range(t):
        n = vals[i]
        i += 1
        out.append(str(solve_case(vals[i:i + n])))
        i += n
    print("\n".join(out))

if __name__ == "__main__":
    main()
