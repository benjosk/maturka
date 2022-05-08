while True:
    try:
        od = int(input("zadaj číslo od: "))
        if od > 30:
            raise ValueError()
        do = int(input("zadaj číslo do: "))
        if do > 30:
            raise ValueError()
        break
    except ValueError:
        print("toto nie je číslo")

if od > do:
    od,do = do,od
k = od
p,q = 0,0
nas = []
zoz = []
print("    ", end="")
for i in range((do-od)+1):
    print(f"{od + i:4}", end="")
print()
print("-" * ((do-od+2)*4))
while k <= do:
    for i in range((do-od)+1):
        nas.append(((od+p)*(od+q)))
        p+= 1
    m = max(nas)
    print(f"{(od+q):2} - ", end ="")
    for daco in nas:
        print(f"{daco:3}", end=" ")
    print()
    nas = []
    k += 1
    p = 0
    q += 1
