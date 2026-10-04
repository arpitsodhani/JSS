# CLAUSE: setup_environment
import sys
import re

sys.setrecursionlimit(1000000)
seed = 123456789

def rnd():
    global seed
    seed += 0x9e3779b97f4a7c15
    x = seed
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb
    return x ^ (x >> 31)

class Atom:
    __slots__ = ("typ", "data", "root", "off", "step", "length")
    def __init__(self, typ, data=None, root=None, off=0, step=1, length=0):
        self.typ = typ
        self.data = data
        self.root = root
        self.off = off
        self.step = step
        self.length = length

class Node:
    __slots__ = ("atom", "left", "right", "prio", "size")
    def __init__(self, atom, left=None, right=None, prio=None):
        self.atom = atom
        self.left = left
        self.right = right
        self.prio = rnd() if prio is None else prio
        self.size = atom.length + size(left) + size(right)

def size(t):
    return t.size if t else 0

def node(a):
    return Node(a) if a and a.length else None

def copy(t, left=None, right=None):
    if left is None:
        left = t.left
    if right is None:
        right = t.right
    return Node(t.atom, left, right, t.prio)

# CLAUSE: solve_logic
def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.prio < b.prio:
        return copy(a, right=merge(a.right, b))
    return copy(b, left=merge(a, b.left))

def split_atom(a, n):
    if n == 0:
        return None, a
    if n == a.length:
        return a, None
    if a.typ == "leaf":
        return Atom("leaf", a.data[:n], length=n), Atom("leaf", a.data[n:], length=a.length - n)
    cut = a.off + (n - 1) * a.step + 1
    left_root, right_root = split(a.root, cut)
    left_atom = Atom("view", root=left_root, off=a.off, step=a.step, length=n) if left_root else None
    right_atom = Atom("view", root=right_root, off=a.step - 1, step=a.step, length=a.length - n) if right_root else None
    return left_atom, right_atom

def split(t, n):
    if not t:
        return None, None
    if n <= 0:
        return None, t
    if n >= t.size:
        return t, None
    ls = size(t.left)
    al = t.atom.length
    if n < ls:
        a, b = split(t.left, n)
        return a, copy(t, left=b)
    if n > ls + al:
        a, b = split(t.right, n - ls - al)
        return copy(t, right=a), b
    if n == ls:
        return t.left, copy(t, left=None)
    if n == ls + al:
        return copy(t, right=None), t.right
    aa, bb = split_atom(t.atom, n - ls)
    return merge(t.left, node(aa)), merge(node(bb), t.right)

def view(t, off, step):
    total = size(t)
    if off >= total:
        return None
    return Node(Atom("view", root=t, off=off, step=step, length=(total - 1 - off) // step + 1))

def first_ge(start, off, step):
    if off >= start:
        return off
    return off + ((start - off + step - 1) // step) * step

def collect_atom(a, first, step, out, limit):
    if a.typ == "leaf":
        out.append(a.data[first::step])
    else:
        collect(a.root, 0, a.off + first * a.step, min(limit, step * a.step), out, limit)

def collect(t, start, off, step, out, limit):
    if not t:
        return
    end = start + t.size
    if first_ge(start, off, step) >= end:
        return
    ls = size(t.left)
    mid = start + ls
    after = mid + t.atom.length
    collect(t.left, start, off, step, out, limit)
    first = first_ge(mid, off, step)
    if first < after:
        collect_atom(t.atom, first - mid, step, out, limit)
    collect(t.right, after, off, step, out, limit)

def main():
    tokens = re.findall(r"[A-Z]+|\d+", sys.stdin.read())
    s, k, m = tokens[0], int(tokens[1]), int(tokens[2])
    root = node(Atom("leaf", s[:k], length=min(len(s), k)))
    p = 3
    for _ in range(m):
        l = int(tokens[p])
        r = int(tokens[p + 1])
        p += 2
        if l > size(root) or r >= k:
            continue
        a, b = split(root, l - 1)
        c, d = split(b, r - l + 1)
        root = merge(a, merge(c, merge(merge(view(c, 1, 2), view(c, 0, 2)), d)))
        root, _ = split(root, k)
    ans = []
    collect(root, 0, 0, 1, ans, k + 1)
    sys.stdout.write("".join(ans)[:k])

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
