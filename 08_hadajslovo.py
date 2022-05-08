import random

def hadaj(slovo):
    zle = 0
    zoz = []
    for pis in slovo:
        zoz.append(pis)
    slovo2 = zoz[0] + ("_"*(len(zoz)-2)) + zoz[-1]
    print(slovo2)
    zoz2 = []
    for pis in slovo2:
        zoz2.append(pis)
    while zle < 11 and "_" in zoz2:
        pismeno = input("dopln pismeno: ")
        if pismeno in zoz[1:-1]:
            ind = zoz.index(pismeno)
            zoz2.pop(ind)
            zoz2.insert(ind,zoz[ind])
            str = ""
            for znak in zoz2:
                str += znak
            print(str)
        else:
            zle += 1
            print("pismeno ", pismeno, " sa tam nenachadza")
    if zle > 10:
        print("neuhadol si :(")
    else:
        print("uhadol si!")
        print("počet zlých odpovedí: ", zle)


slova = ['slnko', 'vietor', 'oblak', 'sneh', 'voda', 'rieka']

hadaj(random.choice(slova))
