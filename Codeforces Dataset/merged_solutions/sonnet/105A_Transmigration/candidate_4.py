import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[str, int]], list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    m = int(numbers[1])
    rate = numbers[2].decode()
    whole, part = rate.split(".") if "." in rate else (rate, "0")
    part = (part + "00")[:2]
    factor = int(whole) * 100 + int(part)
    skills = []
    reader = 3
    for _ in range(n):
        skills.append((numbers[reader].decode(), int(numbers[reader + 1])))
        reader += 2
    wanted = [numbers[reader + i].decode() for i in range(m)]
    return factor, skills, wanted


# --- clause: transmigrate :: (factor: int, skills: list[tuple[str, int]], wanted: list[str]) -> list[tuple[str, int]] ---
def transmigrate(factor, skills, wanted):
    rows = []
    names = set()
    for name, level in skills:
        keep, spare = divmod(level * factor, 100)
        if keep >= 100:
            rows.append((name, keep))
            names.add(name)
    for name in wanted:
        if name not in names:
            rows.append((name, 0))
            names.add(name)
    rows.sort()
    return rows


# --- clause: main :: () -> None ---
def main():
    factor, skills, wanted = read_input()
    rows = transmigrate(factor, skills, wanted)
    out = [str(len(rows))]
    for name, level in rows:
        out.append("%s %d" % (name, level))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
