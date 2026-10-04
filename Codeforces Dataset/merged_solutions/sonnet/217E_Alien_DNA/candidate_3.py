# CLAUSE: setup_environment
import sys
import re

sys.setrecursionlimit(1000000)
state = 987654321

def priority():
    global state
    state = (state + 11995408973635179863) & ((1 << 64) - 1)
    z = state
    z = ((z ^ (z >> 30)) * 13787848793156543929) & ((1 << 64) - 1)
    z = ((z ^ (z >> 27)) * 10723151780598845931) & ((1 << 64) - 1)
    return z ^ (z >> 31)

class Piece:
    __slots__ = ("kind", "value", "tree", "begin", "jump", "count")
    def __init__(self, kind, value="", tree=None, begin=0, jump=1, count=0):
        self.kind = kind
        self.value = value
        self.tree = tree
        self.begin = begin
        self.jump = jump
        self.count = count

class Treap:
    __slots__ = ("piece", "left", "right", "rank", "total")
    def __init__(self, piece, left=None, right=None, rank=None):
        self.piece = piece
        self.left = left
        self.right = right
        self.rank = priority() if rank is None else rank
        self.total = length(left) + piece.count + length(right)

def length(t):
    return 0 if t is None else t.total

def single(piece):
    return Treap(piece) if piece is not None and piece.count > 0 else None

def rebuild(t, left_marker=False, right_marker=False, left=None, right=None):
    if not left_marker:
        left = t.left
    if not right_marker:
        right = t.right
    return Treap(t.piece, left, right, t.rank)

# CLAUSE: solve_logic
def join(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.rank < b.rank:
        return rebuild(a, right_marker=True, right=join(a.right, b))
    return rebuild(b, left_marker=True, left=join(a, b.left))

def divide_piece(piece, take):
    if take <= 0:
        return None, piece
    if take >= piece.count:
        return piece, None
    if piece.kind == "text":
        return Piece("text", piece.value[:take], count=take), Piece("text", piece.value[take:], count=piece.count - take)
    border = piece.begin + (take - 1) * piece.jump + 1
    low, high = cut(piece.tree, border)
    a = Piece("view", tree=low, begin=piece.begin, jump=piece.jump, count=take) if low else None
    b = Piece("view", tree=high, begin=piece.jump - 1, jump=piece.jump, count=piece.count - take) if high else None
    return a, b

def cut(t, take):
    if t is None:
        return None, None
    if take <= 0:
        return None, t
    if take >= t.total:
        return t, None
    left_len = length(t.left)
    here = t.piece.count
    if take < left_len:
        a, b = cut(t.left, take)
        return a, rebuild(t, left_marker=True, left=b)
    if take > left_len + here:
        a, b = cut(t.right, take - left_len - here)
        return rebuild(t, right_marker=True, right=a), b
    if take == left_len:
        return t.left, rebuild(t, left_marker=True, left=None)
    if take == left_len + here:
        return rebuild(t, right_marker=True, right=None), t.right
    p, q = divide_piece(t.piece, take - left_len)
    return join(t.left, single(p)), join(single(q), t.right)

def sampled(t, begin):
    n = length(t)
    if begin >= n:
        return None
    return Treap(Piece("view", tree=t, begin=begin, jump=2, count=(n - 1 - begin) // 2 + 1))

def first_hit(start, residue, gap):
    if residue >= start:
        return residue
    return residue + ((start - residue + gap - 1) // gap) * gap

def emit_piece(piece, local, gap, ans, cap):
    if piece.kind == "text":
        ans.append(piece.value[local::gap])
        return
    emit_tree(piece.tree, 0, piece.begin + local * piece.jump, min(cap, gap * piece.jump), ans, cap)

def emit_tree(t, start, residue, gap, ans, cap):
    stack = [(t, start, 0)]
    while stack:
        node, base, phase = stack.pop()
        if node is None:
            continue
        if first_hit(base, residue, gap) >= base + node.total:
            continue
        left_len = length(node.left)
        piece_start = base + left_len
        piece_end = piece_start + node.piece.count
        if phase == 0:
            stack.append((node.right, piece_end, 0))
            stack.append((node, base, 1))
            stack.append((node.left, base, 0))
        else:
            pos = first_hit(piece_start, residue, gap)
            if pos < piece_end:
                emit_piece(node.piece, pos - piece_start, gap, ans, cap)

def run():
    data = re.findall(r"[A-Z]+|\d+", sys.stdin.read())
    s = data[0]
    k = int(data[1])
    m = int(data[2])
    root = single(Piece("text", s[:k], count=min(k, len(s))))
    pairs = list(map(int, data[3:]))
    for i in range(0, 2 * m, 2):
        l = pairs[i]
        r = pairs[i + 1]
        if l <= length(root) and r < k:
            a, tail = cut(root, l - 1)
            mid, b = cut(tail, r - l + 1)
            add = join(sampled(mid, 1), sampled(mid, 0))
            root = join(a, join(mid, join(add, b)))
            root, tail = cut(root, k)
    out = []
    emit_tree(root, 0, 0, 1, out, k + 1)
    sys.stdout.write("".join(out)[:k])

# CLAUSE: finish_program
if __name__ == "__main__":
    run()
