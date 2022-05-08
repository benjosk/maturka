try:
    a = float(input("strana a v metroch = "))
    b = float(input("strana b v metroch = "))
    c = float(input("strana c v metroch = "))
    if a > 0 and b > 0 and c >0:
        print(f"Cena za takýto pozemok na jeden rok bude {round(a + b + c - 0.5)} eur")
    else:
        raise ValueError
except ValueError:
    print("zlá hodnota")

