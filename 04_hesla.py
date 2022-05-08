import random
# def generuj2(pm,pv,pc,psz):
#     male = "abcdefghijklmnopqrstuvwxyz"
#     velke = male.upper()
#     cisla = "0123456789"
#     speci = "+-*?:_-@#"
#     heslo = ""
#     for i in range(pm):
#         heslo += random.choice(male)
#     for i in range(pv):
#         heslo += random.choice(velke)
#     for i in range(pc):
#         heslo += random.choice(cisla)
#     for i in range(psz):
#         heslo += random.choice(speci)
#     real_heslo= ""
#     while len(heslo) > 0:
#         i = random.randrange(len(heslo))
#         real_heslo += heslo[i]
#         heslo = heslo[:i] + heslo[i+1:]
#     return real_heslo

def generuj(m,v,c,s):
    male = "abcdefghijklmnopqrstuvwxyz"
    velke = male.upper()
    cisla = "0123456789"
    speci = "+-*?:_-@#"
    heslo = []
    for i in range(m):
        heslo.append(random.choice(male))
    for i in range(v):
        heslo.append(random.choice(velke))
    for i in range(c):
        heslo.append(random.choice(cisla))
    for i in range(s):
        heslo.append(random.choice(speci))
    random.shuffle(heslo)
    h = "".join(str(x) for x in heslo)
    return h

pm = int(input("pocet malych pismen: "))
pv = int(input("pocet velkych pismen: "))
pc = int(input("pocet cisel: "))
ps = int(input("pocet specialnych znakov: "))

print(generuj(pm,pv,pc,ps))


