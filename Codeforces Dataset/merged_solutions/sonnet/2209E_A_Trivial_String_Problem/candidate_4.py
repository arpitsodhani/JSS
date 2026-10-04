# CLAUSE: setup_environment
import sys

def z_algorithm(a):
    z = [0] * len(a)
    l = 0
    r = 0
    for i in range(1, len(a)):
        if r >= i:
            z[i] = min(z[i - l], r - i + 1)
        j = z[i]
        while i + j < len(a) and a[j] == a[i + j]:
            j += 1
        z[i] = j
        if i + j - 1 > r:
            l = i
            r = i + j - 1
    if a:
        z[0] = len(a)
    return z

def fill_answers(s, starts, result):
    for left, items in starts.items():
        cur = s[left:]
        z = z_algorithm(cur)
        count = len(cur)
        best_for_len = [0] * (count + 1)
        accumulated = [0] * (count + 1)
        for end in range(1, count + 1):
            chosen = 1
            for split in range(end):
                if z[split] >= end - split:
                    pieces = best_for_len[split] + 1
                    if pieces > chosen:
                        chosen = pieces
            best_for_len[end] = chosen
            accumulated[end] = accumulated[end - 1] + chosen
        for end, index in items:
            result[index] = accumulated[end - left + 1]

# CLAUSE: solve_logic
def run():
    raw = sys.stdin.buffer.read().split()
    p = 0
    cases = int(raw[p])
    p += 1
    output = []
    for _ in range(cases):
        n = int(raw[p])
        q = int(raw[p + 1])
        p += 2
        s = raw[p]
        p += 1
        starts = {}
        result = [0] * q
        for i in range(q):
            l = int(raw[p]) - 1
            r = int(raw[p + 1]) - 1
            p += 2
            if l in starts:
                starts[l].append((r, i))
            else:
                starts[l] = [(r, i)]
        fill_answers(s, starts, result)
        output.extend(str(v) for v in result)
    return "\n".join(output)

# CLAUSE: finish_program
if __name__ == "__main__":
    sys.stdout.write(run())
