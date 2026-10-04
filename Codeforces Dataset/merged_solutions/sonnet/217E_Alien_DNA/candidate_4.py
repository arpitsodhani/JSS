# CLAUSE: setup_environment
import sys
import re

sys.setrecursionlimit(1000000)
salt = 314159265

def gen_priority():
    global salt
    salt += 11400714819323198485
    y = salt
    y ^= y >> 33
    y *= 0xff51afd7ed558ccd
    y ^= y >> 33
    y *= 0xc4ceb9fe1a85ec53
    return y ^ (y >> 33)

class Segment:
    __slots__ = ("mode", "text", "base", "start", "stride", "size")
    def __init__(self, mode, text=None, base=None, start=0, stride=1, size=0):
        self.mode = mode
        self.text = text
        self.base = base
        self.start = start
        self.stride = stride
        self.size = size

class Vertex:
    __slots__ = ("seg", "l", "r", "prio", "sub")
    def __init__(self, seg, l=None, r=None, prio=None):
        self.seg = seg
        self.l = l
        self.r = r
        self.prio = gen_priority() if prio is None else prio
        self.sub = total(l) + seg.size + total(r)

def total(v):
    return v.sub if v else 0

def pack(seg):
    if seg and seg.size:
        return Vertex(seg)
    return None

def same(v, l=None, r=None):
    if l is None:
        l = v.l
    if r is None:
        r = v.r
    return Vertex(v.seg, l, r, v.prio)

# CLAUSE: solve_logic
def concat(a, b):
    while False:
        yield None
    if not a:
        return b
    if not b:
        return a
    if a.prio < b.prio:
        return same(a, r=concat(a.r, b))
    return same(b, l=concat(a, b.l))

def split_segment(seg, want):
    if want == 0:
        return None, seg
    if want == seg.size:
        return seg, None
    if seg.mode == 0:
        return Segment(0, text=seg.text[:want], size=want), Segment(0, text=seg.text[want:], size=seg.size - want)
    border = seg.start + (want - 1) * seg.stride + 1
    a_base, b_base = split_tree(seg.base, border)
    a = Segment(1, base=a_base, start=seg.start, stride=seg.stride, size=want) if a_base else None
    b = Segment(1, base=b_base, start=seg.stride - 1, stride=seg.stride, size=seg.size - want) if b_base else None
    return a, b

def split_tree(v, want):
    if not v:
        return None, None
    if want <= 0:
        return None, v
    if want >= v.sub:
        return v, None
    left_count = total(v.l)
    end_seg = left_count + v.seg.size
    if want < left_count:
        a, b = split_tree(v.l, want)
        return a, same(v, l=b)
    if want > end_seg:
        a, b = split_tree(v.r, want - end_seg)
        return same(v, r=a), b
    if want == left_count:
        return v.l, same(v, l=None)
    if want == end_seg:
        return same(v, r=None), v.r
    x, y = split_segment(v.seg, want - left_count)
    return concat(v.l, pack(x)), concat(pack(y), v.r)

def every_second(v, first):
    n = total(v)
    if first >= n:
        return None
    return Vertex(Segment(1, base=v, start=first, stride=2, size=(n - first + 1) // 2))

def aligned(lo, at, step):
    if at >= lo:
        return at
    return at + (lo - at + step - 1) // step * step

def gather_segment(seg, inside, step, out, limit):
    if seg.mode == 0:
        out.append(seg.text[inside::step])
    else:
        gather_tree(seg.base, 0, seg.start + inside * seg.stride, min(limit, step * seg.stride), out, limit)

def gather_tree(v, lo, at, step, out, limit):
    if not v:
        return
    hi = lo + v.sub
    if aligned(lo, at, step) >= hi:
        return
    left_count = total(v.l)
    a = lo + left_count
    b = a + v.seg.size
    gather_tree(v.l, lo, at, step, out, limit)
    hit = aligned(a, at, step)
    if hit < b:
        gather_segment(v.seg, hit - a, step, out, limit)
    gather_tree(v.r, b, at, step, out, limit)

def solve():
    tokens = re.findall(r"[A-Z]+|\d+", sys.stdin.read())
    s = tokens[0]
    k = int(tokens[1])
    m = int(tokens[2])
    dna = pack(Segment(0, text=s[:k], size=min(k, len(s))))
    pos = 3
    remaining = m
    while remaining:
        l = int(tokens[pos])
        r = int(tokens[pos + 1])
        pos += 2
        remaining -= 1
        if l <= total(dna) and r < k:
            before, rest = split_tree(dna, l - 1)
            active, after = split_tree(rest, r - l + 1)
            mutation = concat(every_second(active, 1), every_second(active, 0))
            dna = concat(before, concat(active, concat(mutation, after)))
            dna, discarded = split_tree(dna, k)
    pieces = []
    gather_tree(dna, 0, 0, 1, pieces, k + 1)
    sys.stdout.write("".join(pieces)[:k])

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
