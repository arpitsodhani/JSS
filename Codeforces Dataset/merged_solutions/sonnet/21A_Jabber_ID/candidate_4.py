import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.readline().strip()


# --- clause: is_word :: (word: str, limit: int) -> bool ---
def is_word(word, limit):
    if len(word) < 1 or len(word) > limit:
        return False
    for ch_here in word:
        if not (ch_here.isalpha() and ch_here.isascii()) and not ch_here.isdigit() and ch_here != "_":
            return False
    return True


# --- clause: is_jabber :: (line: str) -> bool ---
def is_jabber(line):
    parts = line.split("@")
    if len(parts) != 2:
        return False
    name = parts[0]
    tail = parts[1]
    pieces = tail.split("/")
    if len(pieces) > 2:
        return False
    if len(pieces) == 2 and not is_word(pieces[1], 16):
        return False
    host = pieces[0]
    if not is_word(name, 16) or len(host) < 1 or len(host) > 32:
        return False
    words = host.split(".")
    for word in words:
        if not is_word(word, 16):
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_jabber(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
