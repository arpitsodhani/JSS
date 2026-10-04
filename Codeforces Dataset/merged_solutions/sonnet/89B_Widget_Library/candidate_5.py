# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    rows = sys.stdin.read().splitlines()
    if not rows:
        return
    total = int(rows[0].strip())
    kind = {}
    fixed = {}
    border = defaultdict(int)
    spacing = defaultdict(int)
    child_list = defaultdict(list)
    ancestors = defaultdict(set)
    descendants = defaultdict(set)
    names = []

    for row in rows[1:total + 1]:
        line = row.strip()
        if line[:7] == "Widget ":
            body = line[7:]
            a = body.find("(")
            b = body.find(",", a)
            c = body.find(")", b)
            name = body[:a]
            names.append(name)
            kind[name] = "W"
            fixed[name] = (int(body[a + 1:b]), int(body[b + 1:c]))
        elif line[:5] == "HBox ":
            name = line[5:]
            names.append(name)
            kind[name] = "H"
            fixed[name] = (0, 0)
        elif line[:5] == "VBox ":
            name = line[5:]
            names.append(name)
            kind[name] = "V"
            fixed[name] = (0, 0)
        else:
            dot = line.find(".")
            lpar = line.find("(", dot)
            rpar = line.find(")", lpar)
            parent = line[:dot]
            arg = line[lpar + 1:rpar]
            action = line[dot + 1:lpar]
            if action == "pack":
                child = arg
                if child != parent and child not in ancestors[parent]:
                    child_list[parent].append(child)
                    low = set(descendants[child])
                    low.add(child)
                    high = set(ancestors[parent])
                    high.add(parent)
                    for x in low:
                        ancestors[x].update(high)
                    for y in high:
                        descendants[y].update(low)
            elif action == "set_border":
                border[parent] = int(arg)
            else:
                spacing[parent] = int(arg)

    sys.setrecursionlimit(300000)
    cache = {}

    def dimensions(name):
        if name in cache:
            return cache[name]
        if kind[name] == "W":
            result = fixed[name]
        else:
            children = child_list[name]
            if not children:
                result = (0, 0)
            else:
                widths = []
                heights = []
                for child in children:
                    w, h = dimensions(child)
                    widths.append(w)
                    heights.append(h)
                b = border[name] * 2
                gap = spacing[name] * (len(children) - 1)
                if kind[name] == "H":
                    result = (sum(widths) + gap + b, max(heights) + b)
                else:
                    result = (max(widths) + b, sum(heights) + gap + b)
        cache[name] = result
        return result

    lines = []
    for name in sorted(names):
        w, h = dimensions(name)
        lines.append("{} {} {}".format(name, w, h))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
