import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    n = int(lines[0].strip())
    
    names = []
    idx_of = {}
    kind = []
    fixed_w = []
    fixed_h = []
    border = []
    spacing = []
    children = []
    up = []
    down = []
    
    def add_widget(name, typ, w=0, h=0):
        idx_of[name] = len(names)
        names.append(name)
        kind.append(typ)
        fixed_w.append(w)
        fixed_h.append(h)
        border.append(0)
        spacing.append(0)
        children.append([])
        up.append(0)
        down.append(0)
    
    def iter_bits(mask):
        while mask:
            bit = mask & -mask
            yield bit.bit_length() - 1
            mask ^= bit
    
    for line in lines[1:n + 1]:
        line = line.strip()
        
        if line.startswith("Widget "):
            rest = line[7:]
            p = rest.find("(")
            name = rest[:p]
            q = rest.find(",", p)
            r = rest.find(")", q)
            w = int(rest[p + 1:q])
            h = int(rest[q + 1:r])
            add_widget(name, "Widget", w, h)
        
        elif line.startswith("HBox "):
            add_widget(line[5:], "HBox")
        
        elif line.startswith("VBox "):
            add_widget(line[5:], "VBox")
        
        else:
            dot = line.find(".")
            name = line[:dot]
            v = idx_of[name]
            
            if line[dot + 1:].startswith("pack"):
                p = line.find("(", dot)
                q = line.find(")", p)
                child_name = line[p + 1:q]
                c = idx_of[child_name]
                
                if c == v or ((up[v] >> c) & 1):
                    continue
                
                children[v].append(c)
                
                sources = down[c] | (1 << c)
                targets = up[v] | (1 << v)
                
                for x in iter_bits(sources):
                    up[x] |= targets
                for y in iter_bits(targets):
                    down[y] |= sources
            
            elif line[dot + 1:].startswith("set_border"):
                p = line.find("(", dot)
                q = line.find(")", p)
                border[v] = int(line[p + 1:q])
            
            else:
                p = line.find("(", dot)
                q = line.find(")", p)
                spacing[v] = int(line[p + 1:q])
    
    sys.setrecursionlimit(300000)
    memo = {}
    
    def calc(v):
        if v in memo:
            return memo[v]
        
        if kind[v] == "Widget":
            memo[v] = (fixed_w[v], fixed_h[v])
            return memo[v]
        
        if not children[v]:
            memo[v] = (0, 0)
            return memo[v]
        
        sizes = [calc(c) for c in children[v]]
        b = border[v]
        s = spacing[v]
        
        if kind[v] == "HBox":
            width = sum(w for w, h in sizes) + s * (len(sizes) - 1) + 2 * b
            height = max(h for w, h in sizes) + 2 * b
        else:
            width = max(w for w, h in sizes) + 2 * b
            height = sum(h for w, h in sizes) + s * (len(sizes) - 1) + 2 * b
        
        memo[v] = (width, height)
        return memo[v]
    
    out = []
    for name in sorted(names):
        v = idx_of[name]
        w, h = calc(v)
        out.append(f"{name} {w} {h}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
