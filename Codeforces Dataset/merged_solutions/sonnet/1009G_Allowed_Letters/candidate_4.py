# CLAUSE: setup_environment
from sys import stdin, stdout

# CLAUSE: solve_logic
def main():
    data = stdin.buffer.read().split()
    if not data:
        return

    s = data[0]
    n = len(s)
    allowed = [63] * n

    q = int(data[1]) if len(data) > 1 else 0
    j = 2
    for _ in range(q):
        i = int(data[j]) - 1
        mask = 0
        for code in data[j + 1]:
            mask |= 1 << (code - 97)
        allowed[i] = mask
        j += 2

    count = [0] * 6
    for code in s:
        count[code - 97] += 1

    need_inside = [0] * 64
    for x in allowed:
        y = x
        while y < 64:
            need_inside[y] += 1
            y = (y + 1) | x

    have_inside = [0] * 64
    for x in range(1, 64):
        total = 0
        for c, amount in enumerate(count):
            if x >> c & 1:
                total += amount
        have_inside[x] = total

    supersets = [[] for _ in range(64)]
    for x in range(64):
        y = x
        while y < 64:
            supersets[x].append(y)
            y = (y + 1) | x

    masks_with_letter = []
    for c in range(6):
        bit = 1 << c
        masks_with_letter.append([x for x in range(1, 64) if x & bit])

    def works():
        for x in range(1, 64):
            if need_inside[x] > have_inside[x]:
                return False
        return True

    if not works():
        stdout.write("Impossible\n")
        return

    out = []
    for permission in allowed:
        for x in supersets[permission]:
            need_inside[x] -= 1

        for c in range(6):
            if count[c] == 0 or not (permission >> c & 1):
                continue

            count[c] -= 1
            touched = masks_with_letter[c]
            for x in touched:
                have_inside[x] -= 1

            if works():
                out.append(chr(c + 97))
                break

            for x in touched:
                have_inside[x] += 1
            count[c] += 1
        else:
            stdout.write("Impossible\n")
            return

    stdout.write("".join(out) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
