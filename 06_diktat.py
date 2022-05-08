mk, tv = 0,0
m = "iíIÍ"
t = "yýYÝ"
icka = "iíIÍyýYÝ"
veta = "Kobyla býva v modernom obydlí. Sestra je veľmi bystrá."

for i in range (len(veta)):
    if veta[i] in m:
        mk +=1
    elif veta[i] in t:
        tv +=1

for i in range (len(veta)):
    if veta[i] in icka:
        veta = veta[:i] + "_" + veta[i+1:]


print(f"pocet slov: {len(veta.split())}, i/í: {mk}  y/ý: {tv} ,obtiaznost: {round((mk+tv)/len(veta.split()),3)*100}%" )
print(veta)
