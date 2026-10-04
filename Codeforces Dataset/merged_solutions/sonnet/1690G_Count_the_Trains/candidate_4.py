# CLAUSE: setup_environment
import sys

def bit_add(bit, n, i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def bit_sum(bit, i):
    total = 0
    while i > 0:
        total += bit[i]
        i &= i - 1
    return total

def bit_find(bit, n, order):
    pos = 0
    jump = 1 << (n.bit_length() - 1)
    while jump:
        nxt = pos + jump
        if nxt <= n and bit[nxt] < order:
            order -= bit[nxt]
            pos = nxt
        jump >>= 1
    return pos + 1

def activate(bit, active, n, pos):
    active[pos] = 1
    bit_add(bit, n, pos, 1)

def deactivate(bit, active, n, pos):
    active[pos] = 0
    bit_add(bit, n, pos, -1)

# CLAUSE: solve_logic
def run():
    data = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 1
    tests = data[0]
    output = []
    for _ in range(tests):
        n = data[cursor]
        m = data[cursor + 1]
        cursor += 2
        arr = [0] + data[cursor:cursor + n]
        cursor += n
        bit = [0] * (n + 1)
        active = [0] * (n + 1)
        trains = 0
        minimum = 10 ** 40
        for i in range(1, n + 1):
            current = arr[i]
            if current < minimum:
                minimum = current
                activate(bit, active, n, i)
                trains += 1
        pieces = []
        for qi in range(m):
            k = data[cursor]
            d = data[cursor + 1]
            cursor += 2
            arr[k] -= d
            changed = False
            if active[k]:
                changed = True
            else:
                seen = bit_sum(bit, k - 1)
                previous = bit_find(bit, n, seen)
                if arr[k] < arr[previous]:
                    activate(bit, active, n, k)
                    trains += 1
                    changed = True
            if changed:
                kept_left = bit_sum(bit, k)
                while kept_left < trains:
                    right = bit_find(bit, n, kept_left + 1)
                    if arr[right] < arr[k]:
                        break
                    deactivate(bit, active, n, right)
                    trains -= 1
            pieces.append(str(trains))
        output.append(" ".join(pieces))
    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
run()
