# Clause setup_environment [Confidence: 0.80]
import sys


# Clause solve_logic [Confidence: 0.60]
def code(pair):
    if pair == 0:
        return 0
    if pair == 3:
        return 3
    return 1

def flip(pair):
    if pair == 1:
        return 2
    if pair == 2:
        return 1
    return pair

def pair_value(s, i):
    return (ord(s[i]) - 48) * 2 + (ord(s[i + 1]) - 48)

def reverse_block(arr, count):
    arr[:count] = [flip(x) for x in arr[:count][::-1]]

def produce(a, b):
    current = [pair_value(a, i) for i in range(0, len(a), 2)]
    target = [pair_value(b, i) for i in range(0, len(b), 2)]

    have = [0, 0, 0, 0]
    need_count = [0, 0, 0, 0]
    for x in current:
        have[code(x)] += 1
    for x in target:
        need_count[code(x)] += 1
    if have != need_count:
        return None

    result = []
    for pos in range(len(current) - 1, -1, -1):
        if current[pos] == target[pos]:
            continue

        need = code(target[pos])
        chosen = -1

        i = 0
        while i <= pos:
            if code(current[i]) == need:
                if need != 1:
                    chosen = i
                    break
                if i == 0 and flip(current[i]) == target[pos]:
                    chosen = i
                    break
                if i > 0 and current[i] == target[pos]:
                    chosen = i
                    break
            i += 1

        if chosen == -1:
            i = 0
            while i <= pos:
                if code(current[i]) == need:
                    chosen = i
                    break
                i += 1
            result.append(2)
            reverse_block(current, 1)

        if chosen != 0:
            result.append(2 * chosen + 2)
            reverse_block(current, chosen + 1)

        result.append(2 * pos + 2)
        reverse_block(current, pos + 1)

    return result


# Clause finish_program [Confidence: 0.80]
def main():
    items = sys.stdin.read().split()
    if not items:
        return
    total = int(items[0])
    pos = 1
    lines = []
    for _ in range(total):
        answer = plan(items[pos], items[pos + 1])
        pos += 2
        if answer is None:
            lines.append("-1")
        else:
            lines.append(str(len(answer)))
            lines.append(" ".join(str(x) for x in answer))
    print("\n".join(lines))

if __name__ == "__main__":
    main()


