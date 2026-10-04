n = int(input())
for _ in range(n):
    s = input()
    starts_miao = s.startswith("miao. ")
    ends_lala = s.endswith(" lala.")
    
    if starts_miao and ends_lala:
        print("OMG>.< I don't know!")
    elif starts_miao:
        print("Rainbow's")
    elif ends_lala:
        print("Freda's")
    else:
        print("OMG>.< I don't know!")
