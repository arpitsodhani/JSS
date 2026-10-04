# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    text = sys.stdin.read().splitlines()
    if not text:
        return
    m = int(text[0].strip())
    ids = {}
    names = []
    info = []

    def ident(name):
        return ids[name]

    def create(name, kind, w, h):
        ids[name] = len(names)
        names.append(name)
        info.append({"kind": kind, "w": w, "h": h, "b": 0, "s": 0, "c": [], "up": 0, "down": 0})

    def each(mask):
        while mask:
            bit = mask & -mask
            yield bit.bit_length() - 1
            mask ^= bit

    for row in text[1:m + 1]:
        row = row.strip()
        head = row.split(" ", 1)[0]
        if head == "Widget":
            rest = row[7:]
            left = rest.find("(")
            mid = rest.find(",", left)
            right = rest.find(")", mid)
            create(rest[:left], "W", int(rest[left + 1:mid]), int(rest[mid + 1:right]))
        elif head == "HBox":
            create(row[5:], "H", 0, 0)
        elif head == "VBox":
            create(row[5:], "V", 0, 0)
        else:
            dot = row.find(".")
            left = row.find("(", dot)
            right = row.find(")", left)
            name = row[:dot]
            obj = info[ident(name)]
            arg = row[left + 1:right]
            if row[dot + 1:left] == "pack":
                v = ident(name)
                u = ident(arg)
                if u == v or ((info[v]["up"] >> u) & 1):
                    continue
                obj["c"].append(u)
                sources = info[u]["down"] | (1 << u)
                targets = info[v]["up"] | (1 << v)
                for x in each(sources):
                    info[x]["up"] |= targets
                for y in each(targets):
                    info[y]["down"] |= sources
            elif row[dot + 1:left] == "set_border":
                obj["b"] = int(arg)
            else:
                obj["s"] = int(arg)

    state = [0] * len(names)
    ans = [(0, 0)] * len(names)

    for start in range(len(names)):
        if state[start]:
            continue
        stack = [(start, 0)]
        while stack:
            v, phase = stack.pop()
            if phase == 0:
                if state[v] == 2:
                    continue
                state[v] = 1
                stack.append((v, 1))
                for u in info[v]["c"]:
                    if state[u] == 0:
                        stack.append((u, 0))
            else:
                node = info[v]
                if node["kind"] == "W":
                    ans[v] = (node["w"], node["h"])
                elif not node["c"]:
                    ans[v] = (0, 0)
                else:
                    vals = [ans[u] for u in node["c"]]
                    if node["kind"] == "H":
                        ans[v] = (sum(a for a, b in vals) + node["s"] * (len(vals) - 1) + 2 * node["b"], max(b for a, b in vals) + 2 * node["b"])
                    else:
                        ans[v] = (max(a for a, b in vals) + 2 * node["b"], sum(b for a, b in vals) + node["s"] * (len(vals) - 1) + 2 * node["b"])
                state[v] = 2

    output = []
    for name in sorted(names):
        w, h = ans[ids[name]]
        output.append(f"{name} {w} {h}")
    print("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
