
def rozsekaj(text, cislo) :
    i = 0
    while i <= len(text):
        i += cislo
        text = text[:i] + "\n" + text[i:]
        i += 1
    return (text)


x = int(input("cislo:"))
hym = "Nad Tatrou sa blýska, hromy divo bijú, zastavme ich, bratia, veď sa ony stratia, Slováci ožijú."

print(rozsekaj(hym, x))
