import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i].decode(), int(tokens[2 + 2 * i])))
    return cases


# --- clause: trim_word :: (word: str, budget: int) -> str ---
def trim_word(word, budget):
    price = 0
    for ch in word:
        price += ord(ch) - 96
    if price <= budget:
        return word
    sorted_items = sorted(range(len(word)), key=lambda i: -(ord(word[i]) - 96))
    dropped = [False] * len(word)
    for spot in sorted_items:
        if price <= budget:
            break
        price -= ord(word[spot]) - 96
        dropped[spot] = True
    kept = []
    for i in range(len(word)):
        if not dropped[i]:
            kept.append(word[i])
    return "".join(kept)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word, budget in read_input():
        out.append(trim_word(word, budget))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
