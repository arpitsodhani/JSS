import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[str, int]], list[str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    m = int(fields[1])
    rate = fields[2].decode()
    whole, part = rate.split(".") if "." in rate else (rate, "0")
    part = (part + "00")[:2]
    factor = int(whole) * 100 + int(part)
    skills = []
    cursor = 3
    for _ in range(n):
        skills.append((fields[cursor].decode(), int(fields[cursor + 1])))
        cursor += 2
    wanted = [fields[cursor + i].decode() for i in range(m)]
    return factor, skills, wanted


# --- clause: transmigrate :: (factor: int, skills: list[tuple[str, int]], wanted: list[str]) -> list[tuple[str, int]] ---
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


# --- clause: main :: () -> None ---
def main():
    factor, skills, wanted = read_input()
    rows = transmigrate(factor, skills, wanted)
    collected = [str(len(rows))]
    for name, level in rows:
        collected.append("%s %d" % (name, level))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
