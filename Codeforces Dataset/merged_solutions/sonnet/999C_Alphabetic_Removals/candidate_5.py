import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[1]), raw[2].decode()


# --- clause: removal_budget :: (k: int, s: str) -> list[int] ---
def removal_budget(k, s):
    frequency = [0] * 26
    for ch in s:
        frequency[ord(ch) - 97] += 1
    budget = [0] * 26
    for letter in range(26):
        take = frequency[letter] if frequency[letter] < k else k
        budget[letter] = take
        k -= take
        if k == 0:
            break
    return budget


# --- clause: strip_letters :: (s: str, budget: list[int]) -> str ---
def strip_letters(s, budget):
    kept = []
    for ch in s:
        letter = ord(ch) - 97
        if budget[letter]:
            budget[letter] -= 1
        else:
            kept.append(ch)
    return "".join(kept)


# --- clause: main :: () -> None ---
def main():
    k, s = read_input()
    sys.stdout.write(strip_letters(s, removal_budget(k, s)) + "\n")


if __name__ == "__main__":
    main()
