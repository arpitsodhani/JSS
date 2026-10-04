# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def mask_from_word(word):
    value = 0
    for item in word:
        value |= 1 << (item - 97)
    return value

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    name = raw[0]
    size = len(name)
    restricted = int(raw[1]) if len(raw) > 1 else 0
    limits = [63 for _ in range(size)]

    at = 2
    while restricted:
        limits[int(raw[at]) - 1] = mask_from_word(raw[at + 1])
        at += 2
        restricted -= 1

    left = [0, 0, 0, 0, 0, 0]
    for item in name:
        left[item - 97] += 1

    exact = [0] * 64
    for item in limits:
        exact[item] += 1

    contained = [0] * 64
    for group in range(64):
        subtotal = 0
        part = group
        while True:
            subtotal += exact[part]
            if part == 0:
                break
            part = (part - 1) & group
        contained[group] = subtotal

    capacity = [0] * 64
    for group in range(1, 64):
        total = 0
        bit = group
        while bit:
            low = bit & -bit
            total += left[low.bit_length() - 1]
            bit -= low
        capacity[group] = total

    affected_by_rule = [[] for _ in range(64)]
    for rule in range(64):
        for group in range(64):
            if rule & ~group == 0:
                affected_by_rule[rule].append(group)

    affected_by_char = []
    for c in range(6):
        one = 1 << c
        affected_by_char.append([group for group in range(1, 64) if group & one])

    def good():
        return all(contained[group] <= capacity[group] for group in range(1, 64))

    if not good():
        sys.stdout.write("Impossible\n")
        return

    answer = []
    for rule in limits:
        for group in affected_by_rule[rule]:
            contained[group] -= 1

        chosen = -1
        for c in range(6):
            if left[c] > 0 and rule & (1 << c):
                left[c] -= 1
                for group in affected_by_char[c]:
                    capacity[group] -= 1
                if good():
                    chosen = c
                    break
                for group in affected_by_char[c]:
                    capacity[group] += 1
                left[c] += 1

        if chosen < 0:
            sys.stdout.write("Impossible\n")
            return
        answer.append(chr(97 + chosen))

    sys.stdout.write("".join(answer) + "\n")

# CLAUSE: finish_program
main()
