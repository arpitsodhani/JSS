# CLAUSE: setup_environment
import sys

def build_z(text, offset):
    total = len(text) - offset
    z = [0] * total
    lo = 0
    hi = 0
    i = 1
    while i < total:
        if i <= hi:
            span = hi - i + 1
            mirrored = z[i - lo]
            if mirrored < span:
                z[i] = mirrored
            else:
                z[i] = span
        while i + z[i] < total and text[offset + z[i]] == text[offset + i + z[i]]:
            z[i] += 1
        reach = i + z[i] - 1
        if reach > hi:
            lo = i
            hi = reach
        i += 1
    if total:
        z[0] = total
    return z

def prefix_scores(z):
    size = len(z)
    ways = [0] * (size + 1)
    sums = [0] * (size + 1)
    length = 1
    while length <= size:
        best = 1
        prev = 0
        while prev < length:
            need = length - prev
            if z[prev] >= need:
                cand = ways[prev] + 1
                if cand > best:
                    best = cand
            prev += 1
        ways[length] = best
        sums[length] = sums[length - 1] + best
        length += 1
    return sums

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    answer_lines = []
    for _ in range(t):
        n = int(tokens[pos])
        q = int(tokens[pos + 1])
        pos += 2
        s = tokens[pos]
        pos += 1
        head = [-1] * n
        nxt = [-1] * q
        right = [0] * q
        for qi in range(q):
            left = int(tokens[pos]) - 1
            rr = int(tokens[pos + 1]) - 1
            pos += 2
            right[qi] = rr
            nxt[qi] = head[left]
            head[left] = qi
        got = [0] * q
        for left in range(n):
            first = head[left]
            if first == -1:
                continue
            sums = prefix_scores(build_z(s, left))
            qi = first
            while qi != -1:
                got[qi] = sums[right[qi] - left + 1]
                qi = nxt[qi]
        answer_lines += list(map(str, got))
    sys.stdout.write("\n".join(answer_lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
