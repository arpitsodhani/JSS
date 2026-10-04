# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
sys.setrecursionlimit(1000000)
data = sys.stdin.buffer.read().split()
dna = data[0]
k = int(data[1])
n = int(data[2])

class BaseContent:
    __slots__ = ()
BASE = BaseContent()

class MangleContent:
    __slots__ = ('root', 'length')

    def __init__(self, root, length):
        self.root = root
        self.length = length

class Item:
    __slots__ = ('content', 'off', 'length')

    def __init__(self, content, off, length):
        self.content = content
        self.off = off
        self.length = length
seed = 123456789
mask = (1 << 64) - 1

def next_prio():
    global seed
    seed = seed + 11400714819323198485 & mask
    z = seed
    z = (z ^ z >> 30) * 13787848793156543929 & mask
    z = (z ^ z >> 27) * 10723151780598845931 & mask
    return z ^ z >> 31

class Node:
    __slots__ = ('item', 'left', 'right', 'prio', 'total')

    def __init__(self, item, left=None, right=None, prio=None):
        self.item = item
        self.left = left
        self.right = right
        self.prio = next_prio() if prio is None else prio
        self.total = (left.total if left else 0) + item.length + (right.total if right else 0)
sentinel = object()

def clone(node, left=sentinel, right=sentinel):
    return Node(node.item, node.left if left is sentinel else left, node.right if right is sentinel else right, node.prio)

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.prio > b.prio:
        return clone(a, right=merge(a.right, b))
    return clone(b, left=merge(a, b.left))

def split(root, pos):
    if root is None:
        return (None, None)
    left_len = root.left.total if root.left else 0
    item_len = root.item.length
    if pos < left_len:
        a, b = split(root.left, pos)
        return (a, clone(root, left=b))
    if pos > left_len + item_len:
        a, b = split(root.right, pos - left_len - item_len)
        return (clone(root, right=a), b)
    if pos == left_len:
        return (root.left, clone(root, left=None))
    if pos == left_len + item_len:
        return (clone(root, right=None), root.right)
    cut = pos - left_len
    item = root.item
    left_item = Item(item.content, item.off, cut)
    right_item = Item(item.content, item.off + cut, item_len - cut)
    return (merge(root.left, Node(left_item)), merge(Node(right_item), root.right))

def count_less(bound, start, cnt, step):
    if cnt <= 0 or start >= bound:
        return 0
    res = (bound - start + step - 1) // step
    return cnt if res > cnt else res
initial_len = min(k, len(dna))
root = Node(Item(BASE, 0, initial_len))
idx = 3
for _ in range(n):
    l = int(data[idx])
    r = int(data[idx + 1])
    idx += 2
    if r >= k:
        continue
    length = r - l + 1
    a, b = split(root, l - 1)
    mid, c = split(b, length)
    copied = Node(Item(MangleContent(mid, length), 0, length))
    root = merge(a, merge(mid, merge(copied, c)))
    if root.total > k:
        root, _ = split(root, k)
out = []

def emit_content(content, pos, cnt, step):
    if cnt <= 0:
        return
    if content is BASE:
        out.append(dna[pos:pos + step * cnt:step])
        return
    half = content.length // 2
    first = count_less(half, pos, cnt, step)
    if first:
        emit_treap(content.root, 2 * pos + 1, first, 2 * step)
    if first < cnt:
        y = pos + first * step
        emit_treap(content.root, 2 * (y - half), cnt - first, 2 * step)

def emit_item(item, pos, cnt, step):
    emit_content(item.content, item.off + pos, cnt, step)

def emit_treap(node, start, cnt, step):
    if cnt <= 0 or node is None:
        return
    left_len = node.left.total if node.left else 0
    item_len = node.item.length
    left_count = count_less(left_len, start, cnt, step)
    if left_count:
        emit_treap(node.left, start, left_count, step)
    mid_end_count = count_less(left_len + item_len, start, cnt, step)
    if mid_end_count > left_count:
        emit_item(node.item, start + left_count * step - left_len, mid_end_count - left_count, step)
    if mid_end_count < cnt:
        emit_treap(node.right, start + mid_end_count * step - left_len - item_len, cnt - mid_end_count, step)
emit_treap(root, 0, k, 1)
sys.stdout.buffer.write(b''.join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
