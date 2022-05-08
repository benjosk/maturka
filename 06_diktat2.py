with open("vybrane_slova.txt", "r", encoding="utf-8") as subor:
    f = subor.read()

mk, tv = 0,0
icka = "iíIÍyýYÝ"

for znak in f:
    if znak in icka[:4]:
        mk += 1
    elif znak in icka[4:]:
        tv += 1

for i in range(len(f)):
    if f[i] in icka:
        f = f[:i] + "_" + f[i+1:]

print(f"pocet slov: {len(f.split())}, i/í: {mk}  y/ý: {tv} ,obtiaznost: {round((mk+tv)/len(f.split()),3)*100}%" )
print(f)


