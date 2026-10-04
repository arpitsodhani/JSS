import sys


# --- clause: read_input :: () -> tuple[int, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return int(raw[1]), raw[2].decode()


# --- clause: break_period :: (p: int, s: str) -> str | None ---
def break_period(p, s):
    band = list(s)
    n = len(band)
    for i in range(n - p):
        a = band[i]
        b = band[i + p]
        if a != "." and b != "." and a != b:
            broken = True
        elif a == "." and b == ".":
            band[i] = "0"
            band[i + p] = "1"
        elif a == ".":
            band[i] = "1" if b == "0" else "0"
        elif b == ".":
            band[i + p] = "1" if a == "0" else "0"
        else:
            continue
        for j in range(n):
            if band[j] == ".":
                band[j] = "0"
        return "".join(band)
    return None


# --- clause: main :: () -> None ---
def main():
    p, s = read_input()
    result = break_period(p, s)
    sys.stdout.write("No\n" if result is None else result + "\n")


if __name__ == "__main__":
    main()
