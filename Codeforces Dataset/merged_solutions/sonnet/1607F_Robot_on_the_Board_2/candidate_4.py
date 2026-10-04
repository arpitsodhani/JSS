# CLAUSE: setup_environment
import sys

def main():
    raw = sys.stdin.buffer.read().split()
    k = 0
    tests = int(raw[k])
    k += 1
    res = []

# CLAUSE: solve_logic
    for _ in range(tests):
        n = int(raw[k])
        m = int(raw[k + 1])
        k += 2
        cells = raw[k:k + n]
        k += n
        total = n * m

        def jump(v):
            r, c = divmod(v, m)
            ch = cells[r][c]
            if ch == 76:
                return v - 1 if c > 0 else -1
            if ch == 82:
                return v + 1 if c + 1 < m else -1
            if ch == 85:
                return v - m if r > 0 else -1
            return v + m if r + 1 < n else -1

        done = [0] * total
        depth = [0] * total

        for start in range(total):
            if done[start]:
                continue
            local = {}
            seq = []
            v = start
            while v != -1 and not done[v] and v not in local:
                local[v] = len(seq)
                seq.append(v)
                v = jump(v)

            if v == -1:
                cur = 0
                end = len(seq)
            elif done[v]:
                cur = depth[v]
                end = len(seq)
            else:
                begin = local[v]
                cur = len(seq) - begin
                for u in seq[begin:]:
                    depth[u] = cur
                    done[u] = 1
                end = begin

            for idx in range(end - 1, -1, -1):
                cur += 1
                u = seq[idx]
                depth[u] = cur
                done[u] = 1

        mx = -1
        at = 0
        for v in range(total):
            if depth[v] > mx:
                mx = depth[v]
                at = v
        res.append("{} {} {}".format(at // m + 1, at % m + 1, mx))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
