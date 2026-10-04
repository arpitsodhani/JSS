# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.80]
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return
    tests = raw[0]
    at = 1
    lines = []
    for _ in range(tests):
        n = raw[at]
        at += 1
        lines.append(str(answer(raw[at:at + n])))
        at += n
    print("\n".join(lines))

if __name__ == "__main__":
    main()


