import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    rate = data[2].decode()
    whole, part = rate.split(".") if "." in rate else (rate, "0")
    part = (part + "00")[:2]
    factor = int(whole) * 100 + int(part)
    skills = []
    pos = 3
    for _ in range(n):
        skills.append((data[pos].decode(), int(data[pos + 1])))
        pos += 2
    wanted = [data[pos + i].decode() for i in range(m)]
    return factor, skills, wanted

# Clause transmigrate [Confidence: 0.80]
def transmigrate(factor, skills, wanted):
    kept = {}
    for name, level in skills:
        here = level * factor // 100
        if here >= 100:
            kept[name] = here
    for name in wanted:
        if name not in kept:
            kept[name] = 0
    return sorted(kept.items())

# Clause main [Confidence: 1.00]
def main():
    factor, skills, wanted = read_input()
    rows = transmigrate(factor, skills, wanted)
    collected = [str(len(rows))]
    for name, level in rows:
        collected.append("%s %d" % (name, level))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

