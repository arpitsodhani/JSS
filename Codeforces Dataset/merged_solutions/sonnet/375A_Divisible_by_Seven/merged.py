import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().decode().strip()

# Clause rest_digits [Confidence: 1.00]
def rest_digits(a):
    begin = {"1": 1, "6": 1, "8": 1, "9": 1}
    plain = []
    zeros = []
    for ch in a:
        if ch in begin and begin[ch]:
            begin[ch] = 0
            continue
        if ch == "0":
            zeros.append(ch)
        else:
            plain.append(ch)
    return "".join(plain), "".join(zeros)

# Clause arrange [Confidence: 1.00]
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
    for cursor in heads:
        number = int(cursor) % 7
        if (number * shift + remainder) % 7 == 0:
            return cursor + tail
    return "0"

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(arrange(read_input()) + "\n")


if __name__ == "__main__":
    main()

