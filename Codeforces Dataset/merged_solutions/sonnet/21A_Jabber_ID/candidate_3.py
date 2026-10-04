import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.readline().strip()


# --- clause: is_word :: (word: str, limit: int) -> bool ---
def is_word(word, limit):
    if len(word) < 1 or len(word) > limit:
        return False
    for ch_value in word:
        if not (ch_value.isalpha() and ch_value.isascii()) and not ch_value.isdigit() and ch_value != "_":
            return False
    return True


# --- clause: is_jabber :: (line: str) -> bool ---
def is_jabber(line):
    if line.count("@") != 1:
        return False
    name, rest_value = line.split("@")
    if not is_word(name, 16):
        return False
    if "/" in rest_value:
        if rest_value.count("/") != 1:
            return False
        host, resource = rest_value.split("/")
        if not is_word(resource, 16):
            return False
    else:
        host = rest_value
    if len(host) < 1 or len(host) > 32:
        return False
    for word in host.split("."):
        if not is_word(word, 16):
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_jabber(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
