import sys


# --- clause: read_input :: () -> tuple[list[str], list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    m = int(numbers[1])
    stored = [numbers[2 + i].decode() for i in range(n)]
    asked = [numbers[2 + n + i].decode() for i in range(m)]
    return stored, asked


# --- clause: memory_hashes :: (stored: list[str], base: int, mod: int) -> dict[int, set[int]] ---
def memory_hashes(stored, base, mod):
    memory = {}
    for word in stored:
        entry = 0
        for ch in word:
            entry = (entry * base + ord(ch) - 96) % mod
        size = len(word)
        if size not in memory:
            memory[size] = set()
        memory[size].add(entry)
    return memory


# --- clause: has_neighbour :: (word: str, memory: dict[int, set[int]], base: int, mod: int) -> bool ---
def has_neighbour(word, memory, base, mod):
    size = len(word)
    if size not in memory:
        return False
    known = memory[size]
    ahead = [0] * (size + 1)
    power = [1] * (size + 1)
    for i in range(size):
        ahead[i + 1] = (ahead[i] * base + ord(word[i]) - 96) % mod
        power[i + 1] = power[i] * base % mod
    behind = [0] * (size + 1)
    for i in range(size - 1, -1, -1):
        behind[i] = (behind[i + 1] + (ord(word[i]) - 96) * power[size - 1 - i]) % mod
    for i in range(size):
        here = ord(word[i]) - 96
        for other in (1, 2, 3):
            if other == here:
                continue
            head = ahead[i] * power[size - i] % mod
            middle = other * power[size - 1 - i] % mod
            if (head + middle + behind[i + 1]) % mod in known:
                return True
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
