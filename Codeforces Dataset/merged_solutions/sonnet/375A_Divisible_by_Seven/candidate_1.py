import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().decode().strip()


# --- clause: rest_digits :: (a: str) -> tuple[str, str] ---
def rest_digits(a):
    left = {"1": 1, "6": 1, "8": 1, "9": 1}
    plain = []
    zeros = []
    for ch in a:
        if ch in left and left[ch]:
            left[ch] = 0
            continue
        if ch == "0":
            zeros.append(ch)
        else:
            plain.append(ch)
    return "".join(plain), "".join(zeros)


# --- clause: arrange :: (a: str) -> str ---
def arrange(a):
    plain, zeros = rest_digits(a)
    tail = plain + zeros
    remainder = 0
    for ch in tail:
        remainder = (remainder * 10 + int(ch)) % 7
    shift = pow(10, len(tail), 7)
    heads = ["1689", "1698", "1869", "1896", "1968", "1986",
             "6189", "6198", "6819", "6891", "6918", "6981",
             "8169", "8196", "8619", "8691", "8916", "8961",
             "9168", "9186", "9618", "9681", "9816", "9861"]
    for head in heads:
        value = int(head) % 7
        if (value * shift + remainder) % 7 == 0:
            return head + tail
    return "0"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(arrange(read_input()) + "\n")


if __name__ == "__main__":
    main()
