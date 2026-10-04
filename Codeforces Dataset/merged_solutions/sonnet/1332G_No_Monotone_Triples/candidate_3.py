# CLAUSE: setup_environment
import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def sum(self, index):
        result = 0
        while index:
            result += self.tree[index]
            index -= index & -index
        return result

    def lower_bound_from(self, start):
        want = self.sum(start - 1) + 1
        if self.sum(self.n) < want:
            return self.n
        pos = 0
        bit = 1 << self.n.bit_length()
        while bit:
            nxt = pos + bit
            if nxt <= self.n and self.tree[nxt] < want:
                want -= self.tree[nxt]
                pos = nxt
            bit >>= 1
        return pos + 1

def by_value(stack, top, values, pivot, direction):
    left, right = 1, top + 1
    if direction < 0:
        while left < right:
            middle = (left + right) // 2
            if values[stack[middle]] < pivot:
                left = middle + 1
            else:
                right = middle
    else:
        while left < right:
            middle = (left + right) // 2
            if values[stack[middle]] > pivot:
                left = middle + 1
            else:
                right = middle
    return left - 1

def by_position(stack, top, limit):
    left, right = 1, top + 1
    while left < right:
        middle = (left + right) // 2
        if stack[middle] > limit:
            left = middle + 1
        else:
            right = middle
    return left

# CLAUSE: solve_logic
def preprocess(values):
    n = len(values) - 1
    need3 = [n + 1] * (n + 2)
    need4 = [n + 1] * (n + 2)
    pick3 = [(0, 0, 0)] * (n + 2)
    pick4 = [(0, 0, 0, 0)] * (n + 2)
    alive = [0] * (n + 2)
    inc = [0] * (n + 2)
    dec = [0] * (n + 2)
    inc_top = dec_top = inc_run = dec_run = 0
    ready = Fenwick(n + 1)
    ready.add(n + 1, 1)
    for i in range(n, 0, -1):
        while inc_top > 0 and values[inc[inc_top]] > values[i]:
            u = inc[inc_top]
            alive[u] -= 1
            if alive[u] == 0:
                ready.add(u, 1)
            inc_top -= 1
            inc_run = 0
        while dec_top > 0 and values[dec[dec_top]] < values[i]:
            u = dec[dec_top]
            alive[u] -= 1
            if alive[u] == 0:
                ready.add(u, 1)
            dec_top -= 1
            dec_run = 0
        below = by_value(inc, inc_top, values, values[i], -1)
        above = by_value(dec, dec_top, values, values[i], 1)
        end3 = i + max(inc_run, dec_run) + 1
        need3[i] = end3
        pick3[i] = (i, end3 - 1, end3)
        if below and above:
            end4 = ready.lower_bound_from(max(inc[below], dec[above]))
            need4[i] = end4
            if end4 <= n:
                x = inc[by_position(inc, inc_top, end4)]
                y = dec[by_position(dec, dec_top, end4)]
                if x > y:
                    x, y = y, x
                pick4[i] = (i, x, y, end4)
        inc_top += 1
        inc[inc_top] = i
        dec_top += 1
        dec[dec_top] = i
        inc_run += 1
        dec_run += 1
        alive[i] = 2
        if i != n:
            if need3[i] > need3[i + 1]:
                need3[i] = need3[i + 1]
                pick3[i] = pick3[i + 1]
            if need4[i] > need4[i + 1]:
                need4[i] = need4[i + 1]
                pick4[i] = pick4[i + 1]
    return need3, need4, pick3, pick4

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    q = int(raw[1])
    a = [0]
    for i in range(n):
        a.append(int(raw[2 + i]))
    need3, need4, pick3, pick4 = preprocess(a)
    ans = []
    p = n + 2
    for _ in range(q):
        l = int(raw[p])
        r = int(raw[p + 1])
        p += 2
        if need4[l] <= r:
            ans.append("4")
            ans.append("%d %d %d %d" % pick4[l])
        elif need3[l] <= r:
            ans.append("3")
            ans.append("%d %d %d" % pick3[l])
        else:
            ans.append("0")
    sys.stdout.write("\n".join(ans))

main()
