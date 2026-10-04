s = input().strip()
vowels = set("aoyeui")
result = []

for ch in s.lower():
    if ch not in vowels:
        result.append("." + ch)

print("".join(result))
