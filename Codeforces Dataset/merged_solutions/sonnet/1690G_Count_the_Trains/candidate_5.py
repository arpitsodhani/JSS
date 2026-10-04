# CLAUSE: setup_environment
import sys

class Blocks:
    def __init__(self, n):
        self.n = n
        self.width = 450
        self.blocks = (n + self.width - 1) // self.width
        self.on = [0] * (n + 1)
        self.cnt = [0] * self.blocks

    def add(self, pos):
        if self.on[pos] == 0:
            self.on[pos] = 1
            self.cnt[(pos - 1) // self.width] += 1

    def remove(self, pos):
        if self.on[pos]:
            self.on[pos] = 0
            self.cnt[(pos - 1) // self.width] -= 1

    def prev_active(self, pos):
        b = (pos - 1) // self.width
        left = b * self.width + 1
        i = pos
        while i >= left:
            if self.on[i]:
                return i
            i -= 1
        b -= 1
        while b >= 0:
            if self.cnt[b]:
                i = min(self.n, (b + 1) * self.width)
                stop = b * self.width
                while i > stop:
                    if self.on[i]:
                        return i
                    i -= 1
            b -= 1
        return 0

    def next_active(self, pos):
        b = (pos - 1) // self.width
        right = min(self.n, (b + 1) * self.width)
        i = pos
        while i <= right:
            if self.on[i]:
                return i
            i += 1
        b += 1
        while b < self.blocks:
            if self.cnt[b]:
                i = b * self.width + 1
                right = min(self.n, (b + 1) * self.width)
                while i <= right:
                    if self.on[i]:
                        return i
                    i += 1
            b += 1
        return 0

# CLAUSE: solve_logic
def solve():
    ints = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    t = ints[ptr]
    ptr += 1
    all_answers = []
    for _ in range(t):
        n = ints[ptr]
        m = ints[ptr + 1]
        ptr += 2
        a = [0] + ints[ptr:ptr + n]
        ptr += n
        active = Blocks(n)
        last = 10 ** 30
        trains = 0
        for i in range(1, n + 1):
            if a[i] < last:
                last = a[i]
                active.add(i)
                trains += 1
        ans = []
        for _ in range(m):
            k = ints[ptr]
            d = ints[ptr + 1]
            ptr += 2
            a[k] -= d
            if active.on[k] == 0:
                previous = active.prev_active(k - 1)
                if a[k] >= a[previous]:
                    ans.append(str(trains))
                    continue
                active.add(k)
                trains += 1
            nxt = active.next_active(k + 1)
            while nxt:
                if a[nxt] < a[k]:
                    break
                active.remove(nxt)
                trains -= 1
                nxt = active.next_active(nxt + 1)
            ans.append(str(trains))
        all_answers.append(" ".join(ans))
    sys.stdout.write("\n".join(all_answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
