k = 1
e = 0
km = 0
eur = 0
while k == 1:
    n = float(input("zadaj počet prejdených km: "))
    if n <=10:
        e += 0.50
    elif n <=20:
        e += 0.45
    elif n <=30:
        e += 0.40
    elif n >=30:
        e += 0.35
    km += n
    eur += n * e
    print(f"Cena za {km} km je {eur} €")
    if n != 0:
        with open("13_taxicek.txt", "a") as f:
            f.write((str(km) + " " + str(eur) + "\n"))
    e = 0
    if n == 0:
        k -= 1


