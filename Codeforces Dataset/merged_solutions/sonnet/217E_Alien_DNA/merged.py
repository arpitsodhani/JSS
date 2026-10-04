# Clause setup_environment [Confidence: 0.80]
import sys
import re

sys.setrecursionlimit(1000000)
rng = 246813579

def toss():
    global rng
    rng = (rng + 0x9e3779b97f4a7c15) & ((1 << 64) - 1)
    z = rng
    z = ((z ^ (z >> 30)) * 0xbf58476d1ce4e5b9) & ((1 << 64) - 1)
    z = ((z ^ (z >> 27)) * 0x94d049bb133111eb) & ((1 << 64) - 1)
    return z ^ (z >> 31)

class Block:
    __slots__ = ("source", "chars", "tree", "offset", "period", "n")
    def __init__(self, source, chars="", tree=None, offset=0, period=1, n=0):
        self.source = source
        self.chars = chars
        self.tree = tree
        self.offset = offset
        self.period = period
        self.n = n

class Rope:
    __slots__ = ("block", "a", "b", "heap", "n")
    def __init__(self, block, a=None, b=None, heap=None):
        self.block = block
        self.a = a
        self.b = b
        self.heap = toss() if heap is None else heap
        self.n = count(a) + block.n + count(b)

def count(x):
    return x.n if x else 0

def leaf(block):
    if block is None or block.n == 0:
        return None
    return Rope(block)

def reskin(x, a=None, b=None):
    if a is None:
        a = x.a
    if b is None:
        b = x.b
    return Rope(x.block, a, b, x.heap)


# Clause solve_logic [Confidence: 1.00]
def meld(x, y):
    if x is None:
        return y
    if y is None:
        return x
    if x.heap < y.heap:
        return reskin(x, b=meld(x.b, y))
    return reskin(y, a=meld(x, y.a))

def separate_block(block, left_amount):
    if left_amount == 0:
        return None, block
    if left_amount == block.n:
        return block, None
    if block.source == "raw":
        left_text = block.chars[:left_amount]
        right_text = block.chars[left_amount:]
        return Block("raw", left_text, n=len(left_text)), Block("raw", right_text, n=len(right_text))
    boundary = block.offset + (left_amount - 1) * block.period + 1
    left_tree, right_tree = separate(block.tree, boundary)
    left_block = Block("skip", tree=left_tree, offset=block.offset, period=block.period, n=left_amount) if left_tree else None
    right_block = Block("skip", tree=right_tree, offset=block.period - 1, period=block.period, n=block.n - left_amount) if right_tree else None
    return left_block, right_block

def separate(root, left_amount):
    if root is None:
        return None, None
    if left_amount <= 0:
        return None, root
    if left_amount >= root.n:
        return root, None
    na = count(root.a)
    nb = root.block.n
    if left_amount < na:
        x, y = separate(root.a, left_amount)
        return x, reskin(root, a=y)
    if left_amount > na + nb:
        x, y = separate(root.b, left_amount - na - nb)
        return reskin(root, b=x), y
    if left_amount == na:
        return root.a, reskin(root, a=None)
    if left_amount == na + nb:
        return reskin(root, b=None), root.b
    x, y = separate_block(root.block, left_amount - na)
    return meld(root.a, leaf(x)), meld(leaf(y), root.b)

def projection(root, start):
    n = count(root)
    if start >= n:
        return None
    return Rope(Block("skip", tree=root, offset=start, period=2, n=(n - 1 - start) // 2 + 1))

def next_index(lo, residue, step):
    if residue >= lo:
        return residue
    return residue + ((lo - residue + step - 1) // step) * step

def materialize_block(block, start, step, out, cap):
    if block.source == "raw":
        out.append(block.chars[start::step])
    else:
        materialize(block.tree, 0, block.offset + start * block.period, min(cap, step * block.period), out, cap)

def materialize(root, lo, residue, step, out, cap):
    if root is None:
        return
    if next_index(lo, residue, step) >= lo + root.n:
        return
    left_n = count(root.a)
    mid_lo = lo + left_n
    mid_hi = mid_lo + root.block.n
    materialize(root.a, lo, residue, step, out, cap)
    hit = next_index(mid_lo, residue, step)
    if hit < mid_hi:
        materialize_block(root.block, hit - mid_lo, step, out, cap)
    materialize(root.b, mid_hi, residue, step, out, cap)

def main():
    tokens = re.findall(r"[A-Z]+|\d+", sys.stdin.read())
    original = tokens[0]
    k = int(tokens[1])
    m = int(tokens[2])
    rope = leaf(Block("raw", original[:k], n=min(k, len(original))))
    it = 3
    for query in range(m):
        l = int(tokens[it])
        r = int(tokens[it + 1])
        it += 2
        current = count(rope)
        if l > current or r >= k:
            continue
        left, tail = separate(rope, l - 1)
        mid, right = separate(tail, r - l + 1)
        shuffled = meld(projection(mid, 1), projection(mid, 0))
        rope = meld(left, meld(mid, meld(shuffled, right)))
        rope, unused = separate(rope, k)
    out = []
    materialize(rope, 0, 0, 1, out, k + 1)
    sys.stdout.write("".join(out)[:k])


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


