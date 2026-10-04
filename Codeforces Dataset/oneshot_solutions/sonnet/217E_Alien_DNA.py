import sys
import re

sys.setrecursionlimit(1000000)

seed = 123456789

def next_priority():
    global seed
    seed += 0x9e3779b97f4a7c15
    x = seed
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb
    return x ^ (x >> 31)

class Atom:
    __slots__ = ("kind", "data", "root", "offset", "step", "length")
    
    def __init__(self, kind, data=None, root=None, offset=0, step=1, length=0):
        self.kind = kind
        self.data = data
        self.root = root
        self.offset = offset
        self.step = step
        self.length = length

class Node:
    __slots__ = ("atom", "left", "right", "priority", "size")
    
    def __init__(self, atom, left=None, right=None, priority=None):
        self.atom = atom
        self.left = left
        self.right = right
        self.priority = next_priority() if priority is None else priority
        self.size = atom.length + get_size(left) + get_size(right)

def get_size(root):
    return root.size if root else 0

def make_node(atom):
    if atom is None or atom.length == 0:
        return None
    return Node(atom)

def make_view(root, offset, step):
    length = get_size(root)
    if offset >= length:
        return None
    view_len = (length - 1 - offset) // step + 1
    return Node(Atom("view", root=root, offset=offset, step=step, length=view_len))

def clone_node(root, left=None, right=None):
    if left is None:
        left = root.left
    if right is None:
        right = root.right
    return Node(root.atom, left, right, root.priority)

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    
    if a.priority < b.priority:
        return clone_node(a, right=merge(a.right, b))
    return clone_node(b, left=merge(a, b.left))

def split_atom(atom, count):
    if count == 0:
        return None, atom
    if count == atom.length:
        return atom, None
    
    if atom.kind == "leaf":
        return (
            Atom("leaf", data=atom.data[:count], length=count),
            Atom("leaf", data=atom.data[count:], length=atom.length - count)
        )
    
    cut = atom.offset + (count - 1) * atom.step + 1
    left_root, right_root = split(atom.root, cut)
    
    left_atom = None
    if left_root:
        left_len = count
        left_atom = Atom("view", root=left_root, offset=atom.offset,
                         step=atom.step, length=left_len)
    
    right_atom = None
    if right_root:
        right_len = atom.length - count
        right_atom = Atom("view", root=right_root, offset=atom.step - 1,
                          step=atom.step, length=right_len)
    
    return left_atom, right_atom

def split(root, count):
    if not root:
        return None, None
    if count <= 0:
        return None, root
    if count >= root.size:
        return root, None
    
    left_size = get_size(root.left)
    atom_size = root.atom.length
    
    if count < left_size:
        a, b = split(root.left, count)
        return a, clone_node(root, left=b)
    
    if count > left_size + atom_size:
        a, b = split(root.right, count - left_size - atom_size)
        return clone_node(root, right=a), b
    
    if count == left_size:
        return root.left, clone_node(root, left=None)
    
    if count == left_size + atom_size:
        return clone_node(root, right=None), root.right
    
    a_atom, b_atom = split_atom(root.atom, count - left_size)
    left_part = merge(root.left, make_node(a_atom))
    right_part = merge(make_node(b_atom), root.right)
    return left_part, right_part

def first_at_least(start, offset, step):
    if offset >= start:
        return offset
    return offset + ((start - offset + step - 1) // step) * step

def collect_atom(atom, first, step, out, limit):
    if atom.kind == "leaf":
        out.append(atom.data[first::step])
        return
    
    new_offset = atom.offset + first * atom.step
    new_step = step * atom.step
    if new_step > limit:
        new_step = limit
    collect_tree(atom.root, 0, new_offset, new_step, out, limit)

def collect_tree(root, start, offset, step, out, limit):
    if not root:
        return
    
    end = start + root.size
    if first_at_least(start, offset, step) >= end:
        return
    
    left_size = get_size(root.left)
    atom_start = start + left_size
    atom_end = atom_start + root.atom.length
    
    collect_tree(root.left, start, offset, step, out, limit)
    
    first = first_at_least(atom_start, offset, step)
    if first < atom_end:
        collect_atom(root.atom, first - atom_start, step, out, limit)
    
    collect_tree(root.right, atom_end, offset, step, out, limit)

def main():
    text = sys.stdin.read()
    tokens = re.findall(r"[A-Z]+|\d+", text)
    
    s = tokens[0]
    k = int(tokens[1])
    m = int(tokens[2])
    idx = 3
    
    root = make_node(Atom("leaf", data=s[:k], length=min(len(s), k)))
    
    for _ in range(m):
        l = int(tokens[idx])
        r = int(tokens[idx + 1])
        idx += 2
        
        current_len = get_size(root)
        if l > current_len or r >= k:
            continue
        
        left, rest = split(root, l - 1)
        middle, right = split(rest, r - l + 1)
        
        even = make_view(middle, 1, 2)
        odd = make_view(middle, 0, 2)
        copied = merge(even, odd)
        
        root = merge(left, merge(middle, merge(copied, right)))
        root, _ = split(root, k)
    
    result = []
    collect_tree(root, 0, 0, 1, result, k + 1)
    sys.stdout.write("".join(result)[:k])

if __name__ == "__main__":
    main()
