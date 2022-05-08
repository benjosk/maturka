import random

def nazov(n):
    samohlasky = "aeiouáôéíóúäyý"
    spoluhlasky = "hchkgdtnlďťňľdžčžšdzcjbmprsvzĺŕ"
    sam = random.choice(samohlasky)
    spol = random.choice(spoluhlasky)
    naz = ""
    naz += sam.upper() + spol*n + sam
    subor = open("07_nazvy.txt", "r", encoding="utf-8")
    f = subor.read().splitlines()
    subor.close()
    for riadok in f:
        while riadok == naz:
            naz = ""
            print("rovnaky nazov: ", riadok)
            sam = random.choice(samohlasky)
            spol = random.choice(spoluhlasky)
            naz += sam.upper() + spol * n + sam
    return naz


def zapis(poc,n):
    subor = open("07_nazvy.txt", "a", encoding="utf-8")
    for i in range(poc):
        subor.write(nazov(n)+"\n")
    subor.close()


subor = open("07_nazvy.txt", "r", encoding="utf-8")
f = subor.read().splitlines()
pocet = len(f)
print("pocet skupín:", pocet)
subor.close()

n = int(input("pocet pismen v strede: "))
p = int(input("pocet nových skupin: "))
zapis(p,n)
