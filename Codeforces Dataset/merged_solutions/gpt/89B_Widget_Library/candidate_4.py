# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = int(sys.stdin.readline())
    widgets = {}

    for _ in range(n):
        s = sys.stdin.readline().strip()
        if s.startswith("Widget "):
            rest = s[7:]
            name, vals = rest.split("(")
            x, y = map(int, vals[:-1].split(","))
            widgets[name] = ["Widget", x, y, 0, 0, []]
        elif s.startswith("HBox "):
            name = s[5:]
            widgets[name] = ["HBox", 0, 0, 0, 0, []]
        elif s.startswith("VBox "):
            name = s[5:]
            widgets[name] = ["VBox", 0, 0, 0, 0, []]
        else:
            name, action = s.split(".", 1)
            if action.startswith("pack("):
                child = action[5:-1]
                widgets[name][5].append(child)
            elif action.startswith("set_border("):
                widgets[name][3] = int(action[11:-1])
            else:
                widgets[name][4] = int(action[12:-1])

    memo = {}

    def size(name):
        if name in memo:
            return memo[name]

        typ, w, h, border, spacing, children = widgets[name]

        if typ == "Widget":
            memo[name] = (w, h)
            return memo[name]

        if not children:
            memo[name] = (0, 0)
            return memo[name]

        sizes = [size(child) for child in children]

        if typ == "HBox":
            width = sum(x for x, _ in sizes) + 2 * border + spacing * (len(children) - 1)
            height = max(y for _, y in sizes) + 2 * border
        else:
            width = max(x for x, _ in sizes) + 2 * border
            height = sum(y for _, y in sizes) + 2 * border + spacing * (len(children) - 1)

        memo[name] = (width, height)
        return memo[name]

    out = []
    for name in sorted(widgets):
        w, h = size(name)
        out.append(f"{name} {w} {h}")

    print("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
