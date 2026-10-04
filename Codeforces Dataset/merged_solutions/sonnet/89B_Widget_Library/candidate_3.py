# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class Item:
    def __init__(self, kind, w=0, h=0):
        self.kind = kind
        self.w = w
        self.h = h
        self.border = 0
        self.spacing = 0
        self.children = []
        self.parents = set()
        self.kids = set()

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    count = int(lines[0].strip())
    order = []
    items = {}

    for raw in lines[1:count + 1]:
        line = raw.strip()
        if line.startswith("Widget "):
            body = line[7:]
            p = body.find("(")
            q = body.find(",", p)
            r = body.find(")", q)
            name = body[:p]
            items[name] = Item("Widget", int(body[p + 1:q]), int(body[q + 1:r]))
            order.append(name)
        elif line.startswith("HBox "):
            name = line[5:]
            items[name] = Item("HBox")
            order.append(name)
        elif line.startswith("VBox "):
            name = line[5:]
            items[name] = Item("VBox")
            order.append(name)
        else:
            dot = line.find(".")
            name = line[:dot]
            obj = items[name]
            p = line.find("(", dot)
            r = line.find(")", p)
            arg = line[p + 1:r]
            method = line[dot + 1:p]
            if method == "pack":
                child = arg
                if child != name and child not in obj.parents:
                    obj.children.append(child)
                    sources = set(items[child].kids)
                    sources.add(child)
                    targets = set(obj.parents)
                    targets.add(name)
                    for s in sources:
                        items[s].parents.update(targets)
                    for t in targets:
                        items[t].kids.update(sources)
            elif method == "set_border":
                obj.border = int(arg)
            else:
                obj.spacing = int(arg)

    sys.setrecursionlimit(300000)
    memo = {}

    def measure(name):
        if name in memo:
            return memo[name]
        obj = items[name]
        if obj.kind == "Widget":
            ans = (obj.w, obj.h)
        elif not obj.children:
            ans = (0, 0)
        else:
            sizes = [measure(child) for child in obj.children]
            if obj.kind == "HBox":
                ans = (sum(w for w, h in sizes) + obj.spacing * (len(sizes) - 1) + 2 * obj.border, max(h for w, h in sizes) + 2 * obj.border)
            else:
                ans = (max(w for w, h in sizes) + 2 * obj.border, sum(h for w, h in sizes) + obj.spacing * (len(sizes) - 1) + 2 * obj.border)
        memo[name] = ans
        return ans

    result = []
    for name in sorted(order):
        w, h = measure(name)
        result.append(name + " " + str(w) + " " + str(h))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
