import sys


# --- clause: read_input :: () -> tuple[list[str], list[str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    m = int(fields[1])
    stored = [fields[2 + i].decode() for i in range(n)]
    asked = [fields[2 + n + i].decode() for i in range(m)]
    return stored, asked


# --- clause: memory_hashes :: (stored: list[str], base: int, mod: int) -> dict[int, set[int]] ---
def memory_hashes(stored, base, mod):
    memory = {}
    for word in stored:
        element = 0
        for ch in word:
            element = (element * base + ord(ch) - 96) % mod
        length_of = len(word)
        if length_of not in memory:
            memory[length_of] = set()
        memory[length_of].add(element)
    return memory


# --- clause: has_neighbour :: (word: str, memory: dict[int, set[int]], base: int, mod: int) -> bool ---
def has_neighbour(word, memory, base, mod):
    length_of = len(word)
    if length_of not in memory:
        return False
    known = memory[length_of]
    element = 0
    for ch in word:
        element = (element * base + ord(ch) - 96) % mod
    power = 1
    for i in range(length_of - 1, -1, -1):
        here = ord(word[i]) - 96
        for other in (1, 2, 3):
            if other == here:
                continue
            changed = (element + (other - here) * power) % mod
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
