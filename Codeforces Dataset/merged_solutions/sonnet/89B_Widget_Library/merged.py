# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.80]
def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n = int(data[0].strip())
    names = []
    pos = {}
    typ = []
    base = []
    edge = []
    bd = []
    sp = []
    above = []
    below = []

    def new_item(name, kind, w=0, h=0):
        pos[name] = len(names)
        names.append(name)
        typ.append(kind)
        base.append((w, h))
        edge.append([])
        bd.append(0)
        sp.append(0)
        above.append(0)
        below.append(0)

    def bits(mask):
        while mask:
            low = mask & -mask
            yield low.bit_length() - 1
            mask -= low

    for raw in data[1:n + 1]:
        line = raw.strip()
        if line.startswith("Widget "):
            t = line[7:]
            a = t.index("(")
            b = t.index(",", a)
            c = t.index(")", b)
            new_item(t[:a], "W", int(t[a + 1:b]), int(t[b + 1:c]))
        elif line.startswith("HBox "):
            new_item(line[5:], "H")
        elif line.startswith("VBox "):
            new_item(line[5:], "V")
        else:
            d = line.index(".")
            parent = pos[line[:d]]
            tail = line[d + 1:]
            l = line.index("(", d)
            r = line.index(")", l)
            value = line[l + 1:r]
            if tail.startswith("pack"):
                child = pos[value]
                if child != parent and ((above[parent] >> child) & 1) == 0:
                    edge[parent].append(child)
                    src = below[child] | (1 << child)
                    dst = above[parent] | (1 << parent)
                    for x in bits(src):
                        above[x] |= dst
                    for y in bits(dst):
                        below[y] |= src
            elif tail.startswith("set_border"):
                bd[parent] = int(value)
            else:
                sp[parent] = int(value)

    sys.setrecursionlimit(300000)
    memo = [None] * len(names)

    def size(v):
        saved = memo[v]
        if saved is not None:
            return saved
        if typ[v] == "W":
            memo[v] = base[v]
            return memo[v]
        if not edge[v]:
            memo[v] = (0, 0)
            return memo[v]
        got = [size(c) for c in edge[v]]
        b = bd[v]
        s = sp[v]
        if typ[v] == "H":
            ans = (sum(x for x, y in got) + s * (len(got) - 1) + 2 * b, max(y for x, y in got) + 2 * b)
        else:
            ans = (max(x for x, y in got) + 2 * b, sum(y for x, y in got) + s * (len(got) - 1) + 2 * b)
        memo[v] = ans
        return ans

    print("\n".join(f"{name} {size(pos[name])[0]} {size(pos[name])[1]}" for name in sorted(names)))


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


