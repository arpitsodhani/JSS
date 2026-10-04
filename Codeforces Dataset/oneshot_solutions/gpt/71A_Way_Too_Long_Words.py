import sys

data = sys.stdin.read().split()
n = int(data[0])
words = data[1:1 + n]

result = []
for word in words:
    if len(word) > 10:
        result.append(word[0] + str(len(word) - 2) + word[-1])
    else:
        result.append(word)

sys.stdout.write("\n".join(result))
