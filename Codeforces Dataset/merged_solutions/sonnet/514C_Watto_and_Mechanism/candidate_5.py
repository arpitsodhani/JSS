import sys


# --- clause: read_input :: () -> tuple[list[str], list[str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    m = int(raw[1])
    stored = [raw[2 + i].decode() for i in range(n)]
    asked = [raw[2 + n + i].decode() for i in range(m)]
    return stored, asked


# --- clause: memory_hashes :: (stored: list[str], base: int, mod: int) -> dict[int, set[int]] ---
def memory_hashes(stored, base, mod):
    memory = {}
    for word in stored:
        number = 0
        for ch in word:
            number = (number * base + ord(ch) - 96) % mod
        width = len(word)
        if width not in memory:
            memory[width] = set()
        memory[width].add(number)
    return memory


# --- clause: has_neighbour :: (word: str, memory: dict[int, set[int]], base: int, mod: int) -> bool ---
def has_neighbour(word, memory, base, mod):
    width = len(word)
    if width not in memory:
        return False
    known = memory[width]
    number = 0
    for ch in word:
        number = (number * base + ord(ch) - 96) % mod
    power = 1
    for i in range(width - 1, -1, -1):
        here = ord(word[i]) - 96
        for other in (1, 2, 3):
            if other == here:
                continue
            changed = (number + (other - here) * power) % mod
            if changed in known:
                return True
        power = power * base % mod
    return False


# --- clause: main :: () -> None ---
def main():
    stored, asked = read_input()
    base = 131
    mod = (1 << 61) - 1
    memory = memory_hashes(stored, base, mod)
    out = []
    for word in asked:
        out.append("YES" if has_neighbour(word, memory, base, mod) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
