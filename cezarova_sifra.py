def sifruj(sprava,kluc):#vytvorenie funkcie,pozadoane_parametre text a kluc
    sifra = "" #vytvorili sme si prázdnu premennu sifra
    for znak in sprava:#cyklus nam prejde spravu
        if znak == " ":#ak sa znak == prazdnemu miestu
            sifra += znak#tak pokracuj
        elif znak in velke :
            sifra += chr((ord(znak)+kluc-65) % 26 + 65)#ord vytvorí číslo ku kt. + kluc a odpocitame-65 a %26poctom pismen
        elif znak in male:
            sifra += chr((ord(znak)+kluc-97) % 26 + 97)
        elif str(znak) in cisla:
            ind = cisla.index(znak)
            new = ind + kluc
            sifra += cisla[new]
        else:
            sifra += znak
    return sifra

def vstup():
    with open("zasifruj.txt", "r") as subor:
        text = subor.read()
    kluc  = int(input("Zadaj kľúč šifrovania : "))
    while kluc >=27:
        print("Nemožno šifrovať")
        kluc = int(input("Zadaj kľúč : "))
    else:
        print("Zašifrované v súbore zasifruj2.txt")
        with open("zasifruj2.txt", "w") as subor:
            subor.write(sifruj(text,kluc))

velke = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
male = velke.lower()
cisla = ["0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9",
         "0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9"]

vstup()
