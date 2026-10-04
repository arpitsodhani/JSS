import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    word = data[0].decode()
    return word


# --- clause: transform :: (text: str) -> str ---
def transform(text):
    vowels = "aoyeuiAOYEUI"
    kept = [ch.lower() for ch in text if ch not in vowels]
    return "." + ".".join(kept) if kept else ""


# --- clause: main :: () -> None ---
def main():
    print(transform(read_input()))


if __name__ == "__main__":
    main()
