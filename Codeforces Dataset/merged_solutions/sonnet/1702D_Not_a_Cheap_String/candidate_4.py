import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i].decode(), int(numbers[2 + 2 * i])))
    return cases


# --- clause: trim_word :: (word: str, budget: int) -> str ---
def trim_word(word, budget):
    tally = [0] * 27
    price = 0
    for ch in word:
        value = ord(ch) - 96
        tally[value] += 1
        price += value
    drop = [0] * 27
    letter = 26
    while price > budget and letter >= 1:
        while tally[letter] and price > budget:
            tally[letter] -= 1
            drop[letter] += 1
            price -= letter
        letter -= 1
    kept = []
    for ch in word:
        value = ord(ch) - 96
        if drop[value]:
            drop[value] -= 1
        else:
            kept.append(ch)
    return "".join(kept)


# --- clause: main :: () -> None ---
def main():
    out = []
    for word, budget in read_input():
        out.append(trim_word(word, budget))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
