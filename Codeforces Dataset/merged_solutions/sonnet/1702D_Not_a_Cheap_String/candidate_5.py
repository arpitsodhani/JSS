import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i].decode(), int(raw[2 + 2 * i])))
    return cases


# --- clause: trim_word :: (word: str, budget: int) -> str ---
def trim_word(word, budget):
    price = 0
    for ch in word:
        price += ord(ch) - 96
    if price <= budget:
        return word
    queue_order = sorted(range(len(word)), key=lambda i: -(ord(word[i]) - 96))
    dropped = [False] * len(word)
    for spot in queue_order:
        if price <= budget:
            break
        price -= ord(word[spot]) - 96
        dropped[spot] = True
    kept = []
    for i in range(0, len(word)):
        if not dropped[i]:
            kept.append(word[i])
    return "".join(kept)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for word, budget in read_input():
        lines.append(trim_word(word, budget))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
